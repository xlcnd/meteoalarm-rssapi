"""Helper functions."""

from datetime import datetime
from typing import Dict, Tuple

from ._resources import countries as res_countries
from ._resources import regions
from ._webquery import query as wquery
from .exceptions import MeteoAlarmServiceError, MeteoAlarmUnrecognizedCountryError


def cet2iso8601(cet: str) -> str:
    """Transform 'CET strings' to iso8601."""
    buf = cet.replace(" CET", ":00+01:00").replace(" CEST", ":00+02:00")
    return "-".join((buf[6:10], buf[3:5], buf[0:2])) + "T" + buf[11:]


def strdt2iso8601(strdt: str) -> str:
    """Transform 'str dt strings' to iso8601."""
    buf = datetime.strptime(strdt, "%d %b %Y %H:%M:%S %z")
    return str(buf).replace(" ", "T")


def utcnow2iso8601() -> str:
    """Transform 'UTC now dt' to iso8601."""
    return datetime.utcnow().astimezone().replace(microsecond=0).isoformat()


def _days_since(strdt: str) -> int:
    """Calculate days passed from 'strdt strings'."""
    a = datetime.strptime(strdt[0:11], "%d %b %Y")
    b = datetime.today()
    delta = b - a
    return delta.days


def get_regions(country: str) -> Tuple[str, ...]:
    """Return the list of 'regions' for a given country."""
    try:
        return tuple(regions[country].keys())
    except KeyError:
        raise MeteoAlarmUnrecognizedCountryError()


def get_languages(country: str) -> Tuple[str, ...]:
    """Return the list of 'languages' for a given country."""
    try:
        return tuple(res_countries[country][1].split(","))
    except KeyError:
        raise MeteoAlarmUnrecognizedCountryError()


def countries_iso() -> Dict[str, str]:
    """Return a dictionary of countries (k = ISO, v = name)."""
    return {v[0].replace("%20", " ").split("-", 1)[1]: k for k, v in res_countries.items()}


def service_health_check(
    url: str = "http://meteoalarm.eu/robots.txt",
    timeout: int = 2,
) -> bool:
    """Check if the server is responding promptely (2 s)."""
    try:
        wquery(url, timeout)
    except MeteoAlarmServiceError:
        return False
    return True
