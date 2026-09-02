# tests/test_weather_data.py

import numpy as np
import pandas as pd
from unittest.mock import Mock, patch

from src.ingestion.weather_data import get_hourly_data_frame


def create_fake_hourly_response():
    response = Mock()
    hourly = Mock()

    hourly.Time.return_value = 1788300000
    hourly.TimeEnd.return_value = 1788310800
    hourly.Interval.return_value = 3600

    variables = [
        np.array([18.469501, 17.969501, 17.4195]),
        np.array([70.0, 72.0, 75.0]),
        np.array([18.0, 17.5, 17.0]),
    ]

    def get_variable(index):
        variable = Mock()
        variable.ValuesAsNumpy.return_value = variables[index]
        return variable

    hourly.Variables.side_effect = get_variable
    response.Hourly.return_value = hourly

    return response

def test_get_hourly_data_frame_returns_dataframe():
    response = create_fake_hourly_response()

    result = get_hourly_data_frame(response)

    assert isinstance(result, pd.DataFrame)


def test_get_hourly_data_frame_has_expected_columns():
    response = create_fake_hourly_response()

    result = get_hourly_data_frame(response)

    assert list(result.columns) == [
        "date",
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "date_retrieved",
    ]