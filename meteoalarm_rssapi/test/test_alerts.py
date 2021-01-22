#!/usr/bin/env python


from meteoalarm_rssapi import MeteoAlarm


def test_alerts():
    """Minimal test for 'alerts'."""
    meteo = MeteoAlarm('PT', 'COIMBRA')
    print(meteo.alerts())






