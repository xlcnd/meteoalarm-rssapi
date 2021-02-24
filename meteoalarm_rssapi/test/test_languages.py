from meteoalarm_rssapi import MeteoAlarm, get_languages, languages_list


def test_class_languages():
    """Test 'languages' for country from class."""
    meteo = MeteoAlarm("PT", "COIMBRA")
    assert ("pt", "en") == meteo.country_languages()


def test_get_languages():
    """Test 'languages' for country from call."""
    assert get_languages("BE") == ("nl", "fr")


def test_iso_languages():
    """Test 'languages' are  ISO 639-1."""
    ISO_639_1_veted = (
        "bg",
        "bs",
        "cs",
        "de",
        "dk",
        "el",
        "en",
        "es",
        "et",
        "fi",
        "fr",
        "he",
        "hr",
        "hu",
        "is",
        "it",
        "lt",
        "lv",
        "mk",
        "mt",
        "nl",
        "no",
        "pl",
        "pt",
        "ro",
        "sk",
        "sl",
        "sr",
        "sv",
    )
    assert languages_list == ISO_639_1_veted
