#!/usr/bin/env python


from meteoalarm_rssapi import countries_list, country_iso_map


def test_countries_list():
    """Test 'countries_list'."""
    print(countries_list)

def test_country_iso_map():
    """Test 'country_iso_map'."""
    print(country_iso_map())
    print(country_iso_map()['Portugal'])






