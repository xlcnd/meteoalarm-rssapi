from datetime import datetime

from ._resources import countries as res_countries, regions


def cet2iso8601(cet):
    buf = cet.replace(" CET", ":00+01:00").replace(" CEST", ":00+02:00")
    return "-".join((buf[6:10], buf[3:5], buf[0:2])) + "T" + buf[11:]


def strdt2iso8601(strdt):
    buf = datetime.strptime(strdt, "%d %b %Y %H:%M:%S %z")
    return str(buf).replace(" ", "T")


def get_regions(country):
    try:
        return tuple(regions[country].keys())
    except KeyError:
        raise MeteoAlarmUnrecognizedCountryError()


def countries_iso():
    return {
        v[0].replace("%20", " ").split("-", 1)[1]: k for k, v in res_countries.items()
    }
