from ._helpers import get_languages, get_regions, service_health_check
from ._parser import parser
from ._resources import awareness_levels, awareness_types
from ._resources import countries_list as _countries
from ._resources import regions
from .exceptions import (
    MeteoAlarmUnavailableLanguageError,
    MeteoAlarmUnrecognizedCountryError,
    MeteoAlarmUnrecognizedRegionError,
)

TIMEOUT = 20


class MeteoAlarm:
    def __init__(self, country, region, language=None, timeout=TIMEOUT):
        try:
            country = country.upper()
        except AttributeError:
            raise MeteoAlarmUnrecognizedCountryError()
        if country not in _countries:
            raise MeteoAlarmUnrecognizedCountryError()
        self._country = country
        self._region = region
        try:
            code = regions[country][region]
        except KeyError:
            raise MeteoAlarmUnrecognizedRegionError()
        if language:
            language = language.lower()
        if language and language not in get_languages(country):
            raise MeteoAlarmUnavailableLanguageError()
        self._lang = language
        url = "https://www.meteoalarm.eu/documents/rss/{iso}/{country}{code}.rss".format(
            iso=country.lower(), country=country.upper(), code=code,
        )
        self._url = url
        self._timeout = timeout

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

    def country_languages(self):
        return get_languages(self._country)

    def alerts(self):
        return parser(self._url, self._country, self._region, self._lang, self._timeout)
