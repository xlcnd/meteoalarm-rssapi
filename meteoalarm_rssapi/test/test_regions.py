#!/usr/bin/env python


from meteoalarm_rssapi import MeteoAlarm, get_regions


def test_mr_regions():
    """Test 'regions' for countries with many regions."""
    meteo = MeteoAlarm('PT', 'COIMBRA')
    print(meteo.country_regions())

def test_other_regions():
    """Test 'regions' for other countries."""
    print(get_regions('BE'))






