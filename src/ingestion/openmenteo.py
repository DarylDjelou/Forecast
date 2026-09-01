import openmeteo_requests as requests
import pandas as pd
import requests_cache
from retry_requests import retry
import geocoding


url = "https://api.open-meteo.com/v1/forecast"
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = requests.Client(session=retry_session)

def get_weather_response(city_info):
    """
    Get the weather forecast for a given city name.
    :param city_info:
        A dictionary containing the city name, latitude, longitude, and display name.
    :returns:
    the openmeteo response object of the weather forecast for the given city if the city is found, otherwise raises a ValueError.
    """
    latitude = city_info["latitude"]
    longitude = city_info["longitude"]
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": pd.Timestamp.now(tz="UTC").strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hourly": [
            "temperature_2m",
            "relativehumidity_2m",
            "apparent_temperature",
        ],
        "timezone": "auto",
    }
    responses= openmeteo.weather_api(url, params=params)
    return responses[0]