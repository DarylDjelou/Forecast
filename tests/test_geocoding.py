import pytest
from sqlalchemy.sql.operators import isnot

from src.ingestion.geocoding import geocode_city

def test_geocode_city_rejects_empty_string():
    with pytest.raises(ValueError):
        geocode_city("")

def test_geocode_city_rejects_non_string():
    with pytest.raises(ValueError):
        geocode_city(123)

def test_geocode_city_returns_none_for_invalid_city():
    result = geocode_city("InvalidCityNameThatDoesNotExist")
    assert result is None

def test_geocode_city_returns_dict():
    result = geocode_city("Strasbourg")
    assert isinstance(result, dict)
    assert result is not None
    assert "city" in result
    assert "latitude" in result
    assert "longitude" in result
    assert "display_name" in result

