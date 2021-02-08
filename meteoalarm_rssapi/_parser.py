import re

from datetime import datetime
from zlib import crc32

import feedparser

from .exceptions import (
    MeteoAlarmException,
    MeteoAlarmUnrecognizedCountryError,
    MeteoAlarmUnrecognizedRegionError,
    MeteoAlarmParseError,
    MeteoAlarmServiceError,
    MeteoAlarmMissingInfo,
)
from ._helpers import (
    cet2iso8601,
    get_regions,
    service_health_check,
    strdt2iso8601,
)
from ._resources import (
    awareness_levels,
    awareness_types,
    awl,
    awt,
    countries_list as _countries,
    regions,
)
from ._webquery import query


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
)


RE_TR = re.compile(r"<tr(.*?)</tr>", re.I | re.M | re.S)
RE_AWT = re.compile(r'alt="awt:(.*?) ', re.I | re.M | re.S)
RE_AWL = re.compile(r'level:(.*?)"', re.I | re.M | re.S)
RE_FROM = re.compile(r"From: </b><i>(.*?)</i><b>", re.I | re.M | re.S)
RE_UNTIL = re.compile(r"Until: </b><i>(.*?)</i>", re.I | re.M | re.S)
RE_MSG = re.compile(r"<td>(.*?)</td>", re.I | re.M | re.S)
RE_WS = re.compile(r"\s+", re.I | re.M | re.S)
RE_EOL = re.compile(r"\n", re.I | re.M | re.S)


class MeteoAlarm:
    def __init__(self, country, region):
        country = country.upper()
        if country not in _countries:
            raise MeteoAlarmUnrecognizedCountryError()
        self._country = country
        self._region = region
        try:
            code = regions[country][region]
        except KeyError:
            raise MeteoAlarmUnrecognizedRegionError()
        url = "https://www.meteoalarm.eu/documents/rss/{iso}/{country}{code}.rss".format(
            iso=country.lower(), country=country.upper(), code=code
        )
        self._url = url

    @staticmethod
    def countries():
        return _countries

    @staticmethod
    def awareness_levels():
        return awareness_levels

    @staticmethod
    def awareness_types():
        return awareness_types

    def health_check(self, timeout=2):
        return service_health_check(self._url, timeout)

    def country_regions(self):
        return get_regions(self._country)

    def alerts(self):
        try:
            feed = feedparser.parse(query(self._url))

            alerts = [
                entry["description"]
                for entry in feed["entries"]
                if entry["title"] == self._region
            ]
            target = alerts[0] if alerts else ""
            if not target:
                return ()

            pub_date = [
                entry["published"][5:]
                for entry in feed["entries"]
                if entry["title"] == self._region
            ][0]
            # TODO if (now - pub_date) > 3 days => WHITE (missing info)
            # raise MeteoAlarmMissingInfo

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
                    if "No special awareness required" in row:
                        continue
                    msg = RE_MSG.search(row).group(1).strip()
                    msg = re.sub(RE_EOL, " ", msg)
                    msg = re.sub(RE_WS, " ", msg)
                    mcrc = crc32(
                        bytes(
                            self._region
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
                    acrc = crc32(
                        bytes(self._region + atype + from_date[0:5] + msg, "utf-8")
                    )
                    result.append(
                        {
                            "alert_id": acrc,
                            "country": self._country.upper(),
                            "region": self._region,
                            "awareness_type": awt[atype],
                            "awareness_level": awl[alevel][0],
                            "from": cet2iso8601(from_date),
                            "until": cet2iso8601(until_date),
                            "message": msg,
                            "message_id": mcrc,
                            "published": strdt2iso8601(pub_date),
                        },
                    )

            return tuple(sorted(result, key=lambda d: d.get("from")))

        except MeteoAlarmServiceError:
            raise MeteoAlarmServiceError()
        except Exception:
            raise MeteoAlarmParseError()
