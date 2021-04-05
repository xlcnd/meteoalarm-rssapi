"""Query web services."""

import gzip
from io import BytesIO
from socket import timeout as sockettimeout
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .exceptions import MeteoAlarmServiceError

__version__: str = "1.0.6"


UA = f"meteoalarm-rssapi/{__version__} (gzip)"
TIMEOUT: float = 20.0  # seconds


class WEBQuery:
    """Class to query web services."""

    def __init__(self, url: str, timeout: float = TIMEOUT) -> None:
        if not url.lower().startswith("http"):
            raise MeteoAlarmServiceError(f"Url ({url}) not allowed!")
        self._url = url
        self._timeout = timeout
        headers = {"Accept-Encoding": "gzip", "User-Agent": UA}
        self._request = Request(url, headers=headers)

    def response(self):
        """Handle response and errors."""
        try:
            response = urlopen(self._request, timeout=self._timeout)
            return response
        except HTTPError as e:
            raise MeteoAlarmServiceError(f"({e.code}) {e.msg}")
        except URLError as e:
            raise MeteoAlarmServiceError(e.reason)
        except sockettimeout:
            raise MeteoAlarmServiceError("service timeout")
        except TypeError:
            raise MeteoAlarmServiceError("service bad response")

    def data(self) -> bytes:
        """Return the uncompressed data."""
        res = self.response()
        data: bytes
        if res.info().get("Content-Encoding") == "gzip":
            buf = BytesIO(res.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:
            data = res.read()
        return data


def query(url: str, timeout: float = TIMEOUT) -> bytes:
    """Interface function to class WEBQuery."""
    service = WEBQuery(url, timeout)
    return service.data()
