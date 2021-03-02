"""Query web services."""

import gzip
from io import BytesIO
from socket import timeout as sockettimeout
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .exceptions import MeteoAlarmServiceError

__version__ = "1.0.0"


UA = "meteoalarm-rssapi/{version} (gzip)".format(version=__version__)
TIMEOUT = 20


class WEBQuery:
    """Class to query web services."""

    def __init__(self, url, timeout=TIMEOUT):
        if not url.lower().startswith("http"):
            raise MeteoAlarmServiceError("Url (%s) not allowed!" % url)
        self._url = url
        self._timeout = timeout
        headers = {"Accept-Encoding": "gzip", "User-Agent": UA}
        self._request = Request(url, headers=headers)

    def response(self):
        try:
            response = urlopen(self._request, timeout=self._timeout)
        except HTTPError as e:
            raise MeteoAlarmServiceError("(%s) %s" % (e.code, e.msg))
        except URLError as e:
            raise MeteoAlarmServiceError(e.reason)
        except sockettimeout:
            raise MeteoAlarmServiceError("service timeout")
        except TypeError:
            raise MeteoAlarmServiceError("service bad response")
        return response if response else None

    def data(self):
        """Return the uncompressed data."""
        res = self.response()
        if res.info().get("Content-Encoding") == "gzip":
            buf = BytesIO(res.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:
            data = res.read()
        return data


def query(url, timeout=TIMEOUT):
    service = WEBQuery(url, timeout)
    return service.data()
