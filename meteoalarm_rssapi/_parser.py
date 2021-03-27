"""Parse the rss response."""

import re
from typing import Dict, List, Optional, Tuple, Union
from zlib import crc32

from ._helpers import _days_since, cet2iso8601, strdt2iso8601
from ._resources import awl, awl_to_num, awt, countries
from .exceptions import (
    MeteoAlarmMissingInfo,
    MeteoAlarmParseError,
    MeteoAlarmServiceError,
)

# pylint: disable=too-many-locals
GREEN_MESSAGE = "No special awareness required"
DAYS_PAST_TO_WHITE = 3

RE_DESCRIPTION = re.compile(r"<description>(.*?)</description", re.I | re.M | re.S)
RE_PUBDATE = re.compile(r"<pubDate>(.*?)</pubDate>", re.I | re.M | re.S)

RE_TR = re.compile(r"<tr(.*?)</tr>", re.I | re.M | re.S)
RE_AWT = re.compile(r'alt="awt:(.*?) ', re.I | re.M | re.S)
RE_AWL = re.compile(r'level:(.*?)"', re.I | re.M | re.S)
RE_FROM = re.compile(r"From: </b><i>(.*?)</i><b>", re.I | re.M | re.S)
RE_UNTIL = re.compile(r"Until: </b><i>(.*?)</i>", re.I | re.M | re.S)
RE_MSG = re.compile(r"<td>(.*?)</td>", re.I | re.M | re.S)

RE_WS = re.compile(r"\s+", re.I | re.M | re.S)
RE_EOL = re.compile(r"\n", re.I | re.M | re.S)


def clean(msg: str) -> str:
    """Clean the message."""
    msg = re.sub(RE_EOL, " ", msg)
    msg = re.sub(RE_WS, " ", msg)
    msg = msg.replace("\u200b", "").replace("\u200c", "")
    msg = msg.replace("&lt;", "<").replace("&gt;", ">")
    return msg.strip()


# pylint: disable=broad-except
def lang_parser(msg: str, lang: str, country: str) -> Tuple[str, bool]:
    """Parse the message by language if possible."""
    try:
        langs: List[str] = countries[country][1].split(",")
        quirk: List[str] = countries[country][2].split(",")

        # SPECIAL CASE 0
        if not quirk:
            return (msg, False)

        for i, v in enumerate(langs):
            if v == lang:
                idx = i
                break

        # SPECIAL CASE 1
        if len(quirk) == 1:
            if len(langs) == 1:
                parsed = msg.replace(quirk[-1], "").strip(": ")
            else:
                if quirk[-1] in msg:
                    parsed = msg.split(quirk[-1])[idx].strip(": ")
                else:
                    parsed = ""
            return (parsed, True) if parsed else (msg, False)
        # SPECIAL CASE 2
        if idx == len(langs) - 1:
            m = msg.split(quirk[-1])[1]
            parsed = m.replace(quirk[-1], "").strip(": ")
            return (parsed, True) if parsed else (msg, False)
        # NORMAL CASE
        RE_LANG = re.compile(
            r"{}(.*?){}".format(quirk[idx], quirk[idx + 1]),
            re.I | re.M | re.S,
        )
        match = RE_LANG.search(msg)
        if match:
            parsed = match.group(1).strip(": ")
            return (parsed, True)
        return (msg, False)

    except Exception:
        return (msg, False)


# pylint: disable=too-many-branches
def parser(
    rss: str,
    country: str,
    region: str,
    language: Optional[str] = None,
) -> Union[Tuple[()], Tuple[Dict[str, Union[str, int, List[str]]], ...]]:
    """Parse the rss."""
    try:

        # pub_parser & WHITE (missing info)
        match = RE_PUBDATE.search(rss)
        if not match:
            raise MeteoAlarmMissingInfo
        pub_date = match.group(1)[5:]
        if _days_since(pub_date) > DAYS_PAST_TO_WHITE:
            raise MeteoAlarmMissingInfo

        # table_parser
        data = RE_DESCRIPTION.findall(rss)
        table = data[1] if data else ""
        if not table:
            return ()

        # rows_parser
        result: List[Dict[str, Union[str, List[str], int]]] = []
        ids = []
        rows = RE_TR.findall(table)
        rows = [r for r in rows if "Today<" not in r and "Tomorrow<" not in r]
        for i, row in enumerate(rows):

            if i % 2 == 0:
                # get: awt, awl, from and until from rows 0, 2, 4, ...
                try:
                    match = RE_AWT.search(row)
                    atype = match.group(1) if match else ""
                    match = RE_AWL.search(row)
                    alevel = match.group(1) if match else ""
                    match = RE_FROM.search(row)
                    from_date = match.group(1) if match else ""
                    match = RE_UNTIL.search(row)
                    until_date = match.group(1) if match else ""
                    if not all([atype, alevel, from_date, until_date]):
                        raise AttributeError
                except AttributeError:
                    continue
            else:
                # get: msg from rows 1, 3, 5, ...
                if GREEN_MESSAGE in row:
                    continue

                match = RE_MSG.search(row)
                msg = match.group(1) if match else ""
                msg = clean(msg) if match else ""

                if language:
                    msg, status = lang_parser(msg, language, country)
                    language = language if status else ""
                languages: List[str] = (
                    [language] if language else countries[country][1].split(",")
                )

                mcrc = crc32(
                    bytes(
                        region + atype + from_date + until_date + alevel + msg + pub_date,
                        "utf-8",
                    ),
                )
                # filter repeated messages (because today/tomorrow on the site)
                if mcrc in ids:
                    continue
                ids.append(mcrc)

                acrc = crc32(bytes(region + atype + from_date[0:12], "utf-8"))

                result.append(
                    {
                        "alert_id": acrc,
                        "country": country.upper(),
                        "region": region,
                        "awareness_type": awt[atype],
                        "awareness_level": awl[alevel][0],
                        "from": cet2iso8601(from_date),
                        "until": cet2iso8601(until_date),
                        "message": msg,
                        "message_id": mcrc,
                        "published": strdt2iso8601(pub_date),
                        "languages": languages,
                    },
                )

        return tuple(
            sorted(
                result,
                key=lambda d: (d["from"], -awl_to_num[d["awareness_level"]]),  # type: ignore
            ),
        )

    except MeteoAlarmMissingInfo:
        raise MeteoAlarmServiceError()
    except Exception:
        raise MeteoAlarmParseError()
