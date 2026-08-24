import pandas as pd

def get_hourly_data_frame(response):

    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(response.Hourly().Time(), unit="s", utc=True),
            end=pd.to_datetime(response.Hourly().TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=response.Hourly().Interval()),
            inclusive="left"
        ),
        "temperature_2m": response.Hourly().Variables(0).ValuesAsNumpy(),
        "relative_humidity_2m": response.Hourly().Variables(1).ValuesAsNumpy(),
        "apparent_temperature": response.Hourly().Variables(2).ValuesAsNumpy(),
        "date_retrieved": pd.Timestamp.now(tz="UTC")
    }
    hourly_df = pd.DataFrame(hourly_data)
    print(hourly_df)
    return hourly_df

def get_daily_data_frame(response):
    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(response.Daily().Time(), unit="s", utc=True),
            end=pd.to_datetime(response.Daily().TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(days=1),
            inclusive="left"
        ),
        "temperature_2m_max": response.Daily().Variables(0).ValuesAsNumpy(),
        "temperature_2m_min": response.Daily().Variables(1).ValuesAsNumpy(),
        "apparent_temperature_max": response.Daily().Variables(2).ValuesAsNumpy(),
        "apparent_temperature_min": response.Daily().Variables(3).ValuesAsNumpy(),
        "date_retrieved": pd.Timestamp.now(tz="UTC")
    }
    daily_df = pd.DataFrame(daily_data)
    print(daily_df)
    return daily_df