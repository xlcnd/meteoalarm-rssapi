#!/usr/bin/env python


from meteoalarm_rssapi import MeteoAlarm


def test_alerts_coimbra():
    """Minimal test for 'alerts' (PT COIMBRA)."""
    meteo = MeteoAlarm("PT", "COIMBRA")
    print(meteo.alerts())


def test_alerts_isere():
    """Minimal test for 'alerts' (FR Isère)."""
    meteo = MeteoAlarm("FR", "Isère")
    print(meteo.alerts())


def test_alerts_bergland():
    """Minimal test for 'alerts' (DE 'Kreis Bautzen - Bergland')."""
    meteo = MeteoAlarm("DE", "Kreis Bautzen - Bergland")
    print(meteo.alerts())


def test_alerts_gelderland():
    """Minimal test for 'alerts' (NL Gelderland)."""
    meteo = MeteoAlarm("NL", "Gelderland")
    print(meteo.alerts())


def test_alerts_elhierro():
    """Minimal test for 'alerts' (ES 'El Hierro')."""
    meteo = MeteoAlarm("ES", "El Hierro")
    print(meteo.alerts())
