class MeteoAlarmException(Exception):
    """Base class."""

    pass


class MeteoAlarmServiceError(MeteoAlarmException):
    pass


class MeteoAlarmUnrecognizedCountryError(MeteoAlarmException):
    pass


class MeteoAlarmUnrecognizedRegionError(MeteoAlarmException):
    pass


class MeteoAlarmParseError(MeteoAlarmException):
    pass
