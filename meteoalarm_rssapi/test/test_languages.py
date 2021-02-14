#!/usr/bin/env python


from meteoalarm_rssapi import MeteoAlarm, get_languages


def test_class_languages():
    """Test 'languages' for country from class."""
    meteo = MeteoAlarm("PT", "COIMBRA")
    assert ('pt', 'en') == meteo.country_languages()


def test_get_languages():
    """Test 'languages' for country from call."""
    assert get_languages("BE") == ('nl', 'fr')
