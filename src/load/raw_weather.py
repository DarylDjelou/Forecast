import pandas as pd
import sqlalchemy as sa

def weather_dataframe_to_dict(weather_df: pd.DataFrame,location_id: int) -> list[dict]:
    """
    Convert a weather DataFrame to a dictionary.

    Args:
        df (pd.DataFrame): The weather DataFrame to convert.

    Returns:
        dict: A dictionary representation of the DataFrame.
    """
    if not isinstance(weather_df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    return (weather_df.rename(columns={
        "date": "forecast_timestamp",
        "date_retrieved": "retrieved_at",
    }).assign(location_id=location_id)
            .to_dict(orient="records"))

def load_hourly_weather_data(weather_data: list[dict], engine):
    """
    Load hourly weather data into the database.

    Args:
        weather_data (list[dict]): A list of dictionaries containing hourly weather data.
        engine: SQLAlchemy engine for database connection.
    """
    if not isinstance(weather_data, list) or not all(isinstance(item, dict) for item in weather_data):
        raise TypeError("Input must be a list of dictionaries")

    insert_stmt = sa.text("""
        INSERT INTO raw_weather (
            location_id,
            forecast_timestamp,
            temperature_2m,
            relative_humidity_2m,
            apparent_temperature,
            retrieved_at
        )
        VALUES (
            :location_id,
            :forecast_timestamp,
            :temperature_2m,
            :relative_humidity_2m,
            :apparent_temperature,
            :retrieved_at
        )
        ON CONFLICT (location_id, forecast_timestamp, retrieved_at) DO UPDATE SET
            temperature_2m = EXCLUDED.temperature_2m,
            relative_humidity_2m = EXCLUDED.relative_humidity_2m,
            apparent_temperature = EXCLUDED.apparent_temperature
    """)
    with engine.begin() as connection:
        connection.execute(insert_stmt, weather_data)