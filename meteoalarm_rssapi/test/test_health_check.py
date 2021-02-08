#!/usr/bin/env python

import time

from meteoalarm_rssapi import service_health_check


def test_service_health_check():
    """Test service (meteoalarm.eu) health check."""
    try:
        t = time.process_time()
        is_healty = service_health_check()
        assert is_healty
    except ConnectionResetError:
        assert False
    elapsed_time = time.process_time() - t
    millis = int(elapsed_time * 1000)
    assert millis < 1500

