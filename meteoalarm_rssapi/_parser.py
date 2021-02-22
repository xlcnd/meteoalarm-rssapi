import re
from zlib import crc32

import feedparser

from ._helpers import _days_since, cet2iso8601, strdt2iso8601
from ._resources import awl, awl_to_num, awt, countries
from ._webquery import query
from .exceptions import (
    MeteoAlarmException,
    MeteoAlarmMissingInfo,
    MeteoAlarmParseError,
    MeteoAlarmServiceError,
)

KEYS = (
    "alert_id",
    "country",
    "region",
    "awareness_type",
    "awareness_level",
    "from",
    "until",
    "message",
    "message_id",
    "published",
    "languages",
)

GREEN_MESSAGE = "No special awareness required"
DAYS_PAST_TO_WHITE = 3

RE_TR = re.compile(r"<tr(.*?)</tr>", re.I | re.M | re.S)
RE_AWT = re.compile(r'alt="awt:(.*?) ', re.I | re.M | re.S)
RE_AWL = re.compile(r'level:(.*?)"', re.I | re.M | re.S)
RE_FROM = re.compile(r"From: </b><i>(.*?)</i><b>", re.I | re.M | re.S)
RE_UNTIL = re.compile(r"Until: </b><i>(.*?)</i>", re.I | re.M | re.S)
RE_MSG = re.compile(r"<td>(.*?)</td>", re.I | re.M | re.S)
RE_WS = re.compile(r"\s+", re.I | re.M | re.S)
RE_EOL = re.compile(r"\n", re.I | re.M | re.S)


def lang_parser(msg, lang, country):
    try:
        langs = countries.get(country)[1].split(",")
        quirk = countries.get(country)[2].split(",")
        for i, v in enumerate(langs):
            if v == lang:
                idx = i
                break
        # SPECIAL CASE 1
        if len(quirk) == 1:
            if len(langs) == 1:
                return msg.split(quirk[-1])[1].strip(": ")
            return msg.split(quirk[-1])[idx].strip(": ")
        # SPECIAL CASE 2
        if idx == len(langs) - 1:
            m = msg.split(quirk[-1])[1]
            return m.replace(quirk[-1], "").strip(": ")
        # NORMAL CASE
        RE_LANG = re.compile(
            r"{}(.*?){}".format(quirk[idx], quirk[idx + 1]), re.I | re.M | re.S
        )
        return RE_LANG.search(msg).group(1).strip(": ")
    except Exception:
        return ""


def parser(url, country, region, language, timeout):
    try:

        feed = feedparser.parse(query(url, timeout))

        alerts = [
            entry["description"]
            for entry in feed["entries"]
            if entry["title"] == region
        ]
        target = alerts[0] if alerts else ""
        if not target:
            return ()

        pub_date = [
            entry["published"][5:]
            for entry in feed["entries"]
            if entry["title"] == region
        ][0]
        # WHITE (missing info)
        if _days_since(pub_date) > DAYS_PAST_TO_WHITE:
            raise MeteoAlarmMissingInfo

        result = []
        ids = []
        rows = RE_TR.findall(target)
        rows = [r for r in rows if "Today<" not in r and "Tomorrow<" not in r]
        for i, row in enumerate(rows):

            if i % 2 == 0:
                # get: awt, awl, from and until from rows 0, 2, 4, ...
                try:
                    atype = RE_AWT.search(row).group(1)
                    alevel = RE_AWL.search(row).group(1)
                    from_date = RE_FROM.search(row).group(1)
                    until_date = RE_UNTIL.search(row).group(1)
                except AttributeError:
                    continue
            else:
                # get: msg from rows 1, 3, 5, ...
                if GREEN_MESSAGE in row:
                    continue
                msg = RE_MSG.search(row).group(1).strip()
                msg = re.sub(RE_EOL, " ", msg)
                msg = re.sub(RE_WS, " ", msg)
                msg = msg.replace("\u200b", "").replace("\u200c", "")
                if language:
                    msg = lang_parser(msg, language, country)
                mcrc = crc32(
                    bytes(
                        region
                        + atype
                        + from_date
                        + until_date
                        + alevel
                        + msg
                        + pub_date,
                        "utf-8",
                    )
                )
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
                        "languages": [language]
                        if language
                        else countries.get(country)[1].split(","),
                    },
                )

        return tuple(
            sorted(
                result,
                key=lambda d: (d.get("from"), -awl_to_num[d.get("awareness_level")],),
            )
        )

    except (MeteoAlarmMissingInfo, MeteoAlarmServiceError):
        raise MeteoAlarmServiceError()
    except Exception:
        raise MeteoAlarmParseError()
