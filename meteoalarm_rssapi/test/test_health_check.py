from .. import MeteoAlarm, service_health_check


def test_service_health_check_helper():
    """Test service (meteoalarm.eu) health check (helper)."""
    try:
        is_healty = service_health_check()
        assert is_healty
    except ConnectionResetError:
        assert False


def test_service_health_check_class():
    """Test service (meteoalarm.eu) health check (class)."""
    try:
        meteo = MeteoAlarm("PT", "COIMBRA")
        is_healty = meteo.health_check()
        assert is_healty
    except ConnectionResetError:
        assert False
