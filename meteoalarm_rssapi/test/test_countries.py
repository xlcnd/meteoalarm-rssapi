from .. import countries_list, country_iso_map


def test_countries_list():
    """Test 'countries_list'."""
    print(countries_list)


def test_country_iso_map():
    """Test 'country_iso_map'."""
    print(country_iso_map())
    print(country_iso_map()["Portugal"])


def test_iso3166():
    """Test 'countries' are ISO 3166-1 Alpha-2."""
    ISO_3166_1_veted = (
        "AT",
        "BA",
        "BE",
        "BG",
        "CH",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "ES",
        "FI",
        "FR",
        "GR",
        "HR",
        "HU",
        "IE",
        "IL",
        "IS",
        "IT",
        "LT",
        "LU",
        "LV",
        "MD",
        "ME",
        "MK",
        "MT",
        "NL",
        "NO",
        "PL",
        "PT",
        "RO",
        "RS",
        "SE",
        "SI",
        "SK",
        "UK",
    )
    assert countries_list == ISO_3166_1_veted
