#!/usr/bin/env python


from meteoalarm_rssapi import MeteoAlarm


def test_regions():
    """Test import for 'regions'."""
    meteo = MeteoAlarm('PT', 'COIMBRA')
    print(meteo.country_regions())






