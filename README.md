
An API for [meteoalarm.eu](https://www.meteoalarm.eu/) weather alerts.

Lets see a simple example:

```python
from meteoalarm_rssapi import MeteoAlarm
meteo = MeteoAlarm('DE', 'Kreis Ahrweiler')

print(meteo.alerts())
```


and you will get (after some `pprint`):

```
message_id: 1817809724
awareness_type: Snow/Ice
awareness_level: Yellow
country: DE
region: Kreis Ahrweiler
from: 19.01.2021 10:00 CET
until: 19.01.2021 12:00 CET
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

You need to know your iso 2-letter country code (e.g. DE) and the name of your region
**as reported by your national agency to meteoalarm.eu** (e.g. Kreis Ahrweiler). For that, 
please check the page for your country in [meteoalarm.eu](https://www.meteoalarm.eu/).
