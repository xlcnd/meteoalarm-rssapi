import re
import feedparser

from ._resources import awl, awt, regions

# TODO Exceptions...

RE_TODAY = re.compile(r"(Today.*?)>Tomorrow<", re.I | re.M | re.S)
RE_TR = re.compile(r"<tr(.*?)</tr>", re.I | re.M | re.S)
RE_AWT = re.compile(r'alt="awt:(.*?) ', re.I | re.M | re.S)
RE_AWL = re.compile(r'level:(.*?)"', re.I | re.M | re.S)
RE_FROM = re.compile(r"From: </b><i>(.*?)</i><b>", re.I | re.M | re.S)
RE_UNTIL = re.compile(r"Until: </b><i>(.*?)</i>", re.I | re.M | re.S)
RE_MSG = re.compile(r"<td>(.*?)</td>", re.I | re.M | re.S)
RE_WS = re.compile(r"\s+", re.I | re.M | re.S)


def _parser(country, region):
    if country in ("DE", "FR", "SP", "IT"):
        code = regions[country][region]
        url = "https://www.meteoalarm.eu/documents/rss/{iso}/{country}{code}.rss".format(
            iso=country.lower(), country=country.upper(), code=code
        )
    else:
        url = "http://www.meteoalarm.eu/documents/rss/{country}.rss".format(
            country=country.lower()
        )

    feed = feedparser.parse(url)
    alerts = [
        entry["description"] for entry in feed["entries"] if entry["title"] == region
    ]

    target = alerts[0] if alerts else ""
    if not target:
        return ()

    match = RE_TODAY.search(target)
    if not match:
        return ()

    buf = match.group()
    if not buf or "No special awareness required" in buf:
        return ()

    result = []
    rows = RE_TR.findall(buf)
    for i, row in enumerate(rows):

        if i % 2 == 0:
            # get: awt, awl, from and until from rows 0, 2, 4, ...
            atype = RE_AWT.search(row).group(1)
            alevel = RE_AWL.search(row).group(1)
            from_date = RE_FROM.search(row).group(1)
            until_date = RE_UNTIL.search(row).group(1)
        else:
            # get: msg from rows 1, 3, 5, ...
            msg = RE_MSG.search(row).group(1).strip()
            msg = msg.replace(".", ". ").strip()
            msg = re.sub(r"\s+", " ", msg)

            result.append(
                {
                    "country": country.upper(),
                    "region": region,
                    "awareness_type": awt[atype],
                    "awareness_level": awl[alevel][0],
                    "from": from_date,
                    "until": until_date,
                    "message": msg,
                },
            )

    return tuple(result)
