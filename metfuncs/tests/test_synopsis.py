import pytest

import synopsis


@pytest.mark.parametrize(
    "temp_c, wet_bulb_c, dew_point_c, wind_knots_2m, rain_rate, expected_code, expected_text",
    [
        (1, 1,  1, 0, 0, 30, 'FOG'),
        (-1, -1, -1, 0, 0, 31, 'Fog or ice fog in patches'),
        (1, 1, 1, 0, 1.0, 61, 'Rain, not freezing, slight'),
        (1, 1, 1, 0, 3.0, 62, 'Rain, not freezing, moderate'),
        (1, 1, 1, 0, 8.0, 63, 'Rain, not freezing, heavy'),
        (-1, 1, 1, 0, 1.0, 64, 'Rain, freezing, slight'),
        (-1, 1, 1, 0, 3.0, 65, 'Rain, freezing, moderate'),
        (-1, 1, 1, 0, 8.0, 66, 'Rain, freezing, heavy'),
        (10, 12, 13, 6, 0.0, 0, 'No significant weather observed'),
    ]
)
def test_get_synopsis(temp_c, wet_bulb_c, dew_point_c, wind_knots_2m, rain_rate, expected_code, expected_text):
    wmo_4680_code, wmo_4680_text = synopsis.get_synopsis(temp_c, wet_bulb_c, dew_point_c, rain_rate, wind_knots_2m)

    assert wmo_4680_code == expected_code
    assert wmo_4680_text == expected_text
