class MeteoAlarmException(Exception):
    """Base class."""


class MeteoAlarmServiceError(MeteoAlarmException):
    pass


class MeteoAlarmUnrecognizedCountryError(MeteoAlarmException):
    pass


class MeteoAlarmUnrecognizedRegionError(MeteoAlarmException):
    pass


class MeteoAlarmUnavailableLanguageError(MeteoAlarmException):
    pass


class MeteoAlarmParseError(MeteoAlarmException):
    pass


class MeteoAlarmMissingInfo(MeteoAlarmException):
    pass
