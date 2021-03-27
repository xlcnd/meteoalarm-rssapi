"""Main class to interact with the 'meteoalarm' service."""
from typing import Dict, List, Optional, Tuple, Union

from ._helpers import get_languages, get_regions, service_health_check
from ._parser import parser
from ._resources import awareness_levels, awareness_types
from ._resources import countries_list as _countries
from ._resources import regions
from ._webquery import query
from .exceptions import (
    MeteoAlarmServiceError,
    MeteoAlarmUnavailableLanguageError,
    MeteoAlarmUnrecognizedCountryError,
    MeteoAlarmUnrecognizedRegionError,
)

TIMEOUT: float = 20.0  # seconds


class MeteoAlarm:
    """Main class to interact with the 'meteoalarm' service."""

    def __init__(
        self,
        country: str,
        region: str,
        language: Optional[str] = None,
        timeout: float = TIMEOUT,
    ) -> None:
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
        iso = country.lower()
        url = f"https://www.meteoalarm.eu/documents/rss/{iso}/{country}{code}.rss"
        self._url = url
        self._timeout = timeout

    @staticmethod
    def countries() -> Tuple[str, ...]:
        """Return the list of the participating countries (ISO 3166-1 Alpha-2)."""
        return _countries

    @staticmethod
    def awareness_types() -> Tuple[str, ...]:
        """Return the list of 'awareness types' (events)."""
        return awareness_types

    @staticmethod
    def awareness_levels() -> Tuple[Tuple[str, str], ...]:
        """Return the list of 'awareness levels' (severity)."""
        return awareness_levels

    def country_regions(self) -> Tuple[str, ...]:
        """Return the list of 'regions' for the country."""
        return get_regions(self._country)

    def country_languages(self) -> Tuple[str, ...]:
        """Return the list of 'languages' for the country."""
        return get_languages(self._country)

    def alerts(self) -> Union[Tuple[()], Tuple[Dict[str, Union[str, int, List[str]]], ...]]:
        """Return the list of 'alerts' currently available."""
        try:
            tmfast = 0.3 * self._timeout
            data: bytes = query(self._url, timeout=tmfast) or bytes("", "utf-8")
            if not data:
                tmslow = 0.7 * self._timeout
                data = query(self._url, timeout=tmslow)
            if not data:
                return ()
            rss = data.decode("UTF-8", "ignore")
            if not rss:
                return ()
        except MeteoAlarmServiceError:
            raise MeteoAlarmServiceError()
        return parser(rss, self._country, self._region, self._lang)

    def health_check(self, timeout: float = 2) -> bool:
        """Verify if the server is responding."""
        return service_health_check(self._url, timeout)
