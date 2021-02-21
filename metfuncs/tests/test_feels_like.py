import pytest

import feels_like


# vTemperature = 35.0
# vWindSpeed = 10.0
# vRelativeHumidity = 72.0
@pytest.mark.parametrize(
    "temp_f, wind_mph, humidity, expected",
    [
        (35.0, 10.0,  72.0, 27.4),
    ]
)
def test_feels_like(temp_f, wind_mph, humidity, expected):
    feels_like_f = feels_like.feels_like(temp_f, wind_mph, humidity)

    assert feels_like_f == expected



