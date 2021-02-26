import pytest

import fog


@pytest.mark.parametrize(
    "temp_c, dew_point_c, wet_bulb_c, wind_knots_2m, solar, expected",
    [
        (1, 1, 1, 1.0, 1, True),
        (-1, -1, -1, 1.0, 1, True),
        (-1, -1, -1, 2.0, 1, False),
        (-1, -1, -3, 1.0, 1, False),
        (10, 20, 30, 1.0, 1, False),
    ]
)
def test_fog_1(temp_c, dew_point_c, wet_bulb_c, wind_knots_2m, solar, expected):
    is_fog = fog.fog_algo_1(temp_c, dew_point_c, wet_bulb_c, wind_knots_2m, solar)

    assert is_fog == expected


@pytest.mark.parametrize(
    "temp_c, dew_point_c, wind_knots_2m, expected",
    [
        (1, 1, 1.0, True),
        (1, 1, 3.0, False),
        (-1, -1, 1.0, True),
        (-1, -1, 2.0, False),
        (-1, -1, 1.0, True),
        (-1, 1.4, 1.0, True),
        (-1, 1.5, 1.0, False),
        (-1, 1.7, 1.0, False),
        (10, 20, 1.0, False),
    ]
)
def test_fog_2(temp_c, dew_point_c, wind_knots_2m, expected):
    is_fog = fog.fog_algo_2(temp_c, dew_point_c, wind_knots_2m)

    assert is_fog == expected
