#!/usr/bin/env python


from meteoalarm_rssapi import MeteoAlarm, get_regions


def test_mr_regions():
    """Test 'regions' for country from class."""
    meteo = MeteoAlarm('PT', 'COIMBRA')
    print(meteo.country_regions())

def test_other_regions():
    """Test 'regions' for country from call."""
    print(get_regions('BE'))






