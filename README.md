[![GitHub tests](https://github.com/xlcnd/meteoalarm-rssapi/workflows/tests/badge.svg)][2]
[![GitHub issues by-label](https://img.shields.io/github/issues/xlcnd/meteoalarm-rssapi/bug?label=bugs)][3]
[![PyPI](https://img.shields.io/pypi/v/meteoalarm-rssapi)][1]
[![PyPI - Downloads](https://img.shields.io/pypi/dm/meteoalarm-rssapi)][1]

An API for [meteoalarm.eu](https://www.meteoalarm.eu/) weather alerts.


> *DISCLAIMER: This is an open source project and doesn't have any affiliation with [meteoalarm.eu](https://www.meteoalarm.eu/)*.


To install enter in a command line:

```bash
pip install meteoalarm-rssapi
```

Now, lets see a simple example:

```python
from meteoalarm_rssapi import MeteoAlarm

meteo = MeteoAlarm("DE", "Kreis Ahrweiler", "de")

print(meteo.alerts())
```


and you will get (after some `pprint`):

```
  alert_id: 507556137
  awareness_level: Yellow
  awareness_type: Extreme low temperature
  country: DE
  region: Kreis Ahrweiler
  from: 2021-02-13T18:00:00+01:00
  until: 2021-02-14T12:00:00+01:00
  languages: ['de']
  message: Es tritt mäßiger Frost zwischen -7 °C und -9 °C auf. In
           Bodennähe wird strenger Frost um -12 °C erwartet.
  message_id: 3743141168
  published: 2021-02-14T01:00:00+01:00
```


You need to know your [ISO 3166-1 Alpha-2][5] country code (e.g. DE) and the **exact name** of your region **as reported by your national agency to meteoalarm.eu** (e.g. Kreis Ahrweiler). For that, please check the page for your country in [meteoalarm.eu](https://www.meteoalarm.eu/), or run the following script:

```python
from meteoalarm_rssapi import get_regions

print(get_regions("DE"))
```
You need to know the [ISO 639-1 code][4] for the message's language (usually the languages available for each country are english ('en') and the local language ('de')). The indication of **language is optional**, and if no language is specified the message will come unparsed and in all available languages.

The timestamps for `published`, `from` and `until` are in ISO8601 format, so that you can (*easily*) convert them to your local date/time.


There are two pieces of information that could be important for your applications:

1. `alert_id` changes to a new value (for a given `awareness_type`) when there is a change in the day/month or first digit of hour of `from`. So, doesn't change if there are only a revision of the H:MM, a revision for `until` or a change in the `awareness_level`.
2. `message_id` changes with any change in `message`, `published`, `from`, `until` or `awareness_level`.

In conclusion, for one `alert_id` there are several `message_id` (that can be taken as the revisions of the `alert_id`).


[1]: https://pypi.org/project/meteoalarm-rssapi/
[2]: https://github.com/xlcnd/meteoalarm-rssapi/actions
[3]: https://github.com/xlcnd/meteoalarm-rssapi/issues?q=is%3Aissue+is%3Aopen+label%3Abug
[4]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[5]: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
