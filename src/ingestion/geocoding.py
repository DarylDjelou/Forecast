from typing import Any

from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="Forecast")


def geocode_city(city_name)-> dict[str, str | Any] | None:
    """
    Geocode a city name to get its latitude and longitude.

    Args:
        city_name (str): The name of the city to geocode.
    Returns:
        dict: A dictionary containing the city name, latitude, longitude, and display name if found, otherwise None.
    """

    if not isinstance(city_name, str) or not city_name.strip():
        raise ValueError("city must be a non-empty string")
    try:
        location = geolocator.geocode(city_name,
                                       featuretype="city",
                                       exactly_one=True,
                                       addressdetails=True,
                                       timeout=10)
    except Exception as e:
        print(f"Error geocoding city '{city_name}': {e}")
        return None
    if location  is None:
        return None
    return {
        "city": city_name,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "display_name": location.address
    }