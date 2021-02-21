from datetime import datetime

from ._resources import countries as res_countries
from ._resources import regions
from ._webquery import query as wquery
from .exceptions import MeteoAlarmServiceError, MeteoAlarmUnrecognizedCountryError


def cet2iso8601(cet):
    buf = cet.replace(" CET", ":00+01:00").replace(" CEST", ":00+02:00")
    return "-".join((buf[6:10], buf[3:5], buf[0:2])) + "T" + buf[11:]


def strdt2iso8601(strdt):
    buf = datetime.strptime(strdt, "%d %b %Y %H:%M:%S %z")
    return str(buf).replace(" ", "T")


def utcnow2iso8601():
    return datetime.utcnow().astimezone().replace(microsecond=0).isoformat()


def _days_since(strdt):
    a = datetime.strptime(strdt[0:11], "%d %b %Y")
    b = datetime.today()
    delta = b - a
    return delta.days


def get_regions(country):
    try:
        return tuple(regions[country].keys())
    except KeyError:
        raise MeteoAlarmUnrecognizedCountryError()


def get_languages(country):
    try:
        return tuple(res_countries[country][1].split(","))
    except KeyError:
        raise MeteoAlarmUnrecognizedCountryError()


def countries_iso():
    return {
        v[0].replace("%20", " ").split("-", 1)[1]: k for k, v in res_countries.items()
    }


def service_health_check(url="http://meteoalarm.eu/robots.txt", timeout=2):
    try:
        wquery(url, timeout)
    except MeteoAlarmServiceError:
        return False
    return True
