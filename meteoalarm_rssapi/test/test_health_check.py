#!/usr/bin/env python

from meteoalarm_rssapi import service_health_check


def test_service_health_check():
    """Test service (meteoalarm.eu) health check."""
    try:
        is_healty = service_health_check()
        assert is_healty
    except ConnectionResetError:
        assert False

