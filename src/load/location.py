import sqlalchemy as sa
from src.database.connection import engine

def load_location_data(location: dict):
    """
    Load location data into the database.

    Args:
        location (dict): A dictionary containing location data with keys 'city', 'latitude', 'longitude', and 'timezone'.
    """

    required_keys = {'city', 'latitude', 'longitude', 'timezone'}
    if not required_keys.issubset(location.keys()):
        raise ValueError(f"Missing required keys in location_data. Required keys: {required_keys}")

    insert_stmt = sa.text("""
        INSERT INTO location (city, latitude, longitude, timezone)
        VALUES (:city, :latitude, :longitude, :timezone)
        ON CONFLICT (city) DO UPDATE SET
            latitude = EXCLUDED.latitude,
            longitude = EXCLUDED.longitude,
            timezone = EXCLUDED.timezone
    """)
    with engine.begin() as connection:
        connection.execute(insert_stmt, location)