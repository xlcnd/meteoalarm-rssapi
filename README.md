![tests](https://github.com/xlcnd/meteoalarm-rssapi/workflows/tests/badge.svg)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/xlcnd/meteoalarm-rssapi?label=version&sort=semver)

An API for [meteoalarm.eu](https://www.meteoalarm.eu/) weather alerts.

To install enter in a command line:

```
pip install meteoalarm-rssapi
```

Now, lets see a simple example:

```python
from meteoalarm_rssapi import MeteoAlarm
meteo = MeteoAlarm('DE', 'Kreis Ahrweiler')

print(meteo.alerts())
```


and you will get (after some `pprint`):

```
alert_id: 3820923534
message_id: 1817809724
awareness_type: Snow/Ice
awareness_level: Yellow
country: DE
region: Kreis Ahrweiler
from: 2021-01-26T18:00:00+01:00
until: 2021-01-27T11:00:00+01:00
message:
  deutsch: Es tritt im Warnzeitraum oberhalb 400 m leichter
  Schneefall mit Mengen zwischen 1 cm und 3 cm auf. In Staulagen
  werden Mengen bis 5 cm erreicht. Die Schneefallgrenze steigt auf
  1500 Meter. Verbreitet wird es glatt.
  english: There is a risk of light snowfall (Level 1 of 4).
  Height range: > 400 m;
  Precipitation amounts: 1-3 cm; in windward areas: < 5 cm;
  snowfall level: rising to 1500 meter
```


You need to know your iso 2-letter country code (e.g. DE) and the **exact name** of your region
**as reported by your national agency to meteoalarm.eu** (e.g. Kreis Ahrweiler). For that, 
please check the page for your country in [meteoalarm.eu](https://www.meteoalarm.eu/).


The timestamps for `from` and `until` are in format ISO8601 so that you can 
(*easily*) convert them to your local date/time. 


There are two pieces of information that could be important for your applications:

1. `alert_id` changes to a new value when there is a change in the `message` or in the 
   day/month of `from`. So, doesn't change if there are only a revision of the H:M, a revision
   for `until` or a change in the `awareness_level`.
2. `message_id` changes with any change in `message`, `from`, `until` or `awareness_level`.

In conclusion, for one `alert_id` there are several `message_id` 
(that can be taken as the revisions of the `alert_id`).
