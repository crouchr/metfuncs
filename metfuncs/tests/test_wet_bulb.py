import pytest

import wet_bulb


@pytest.mark.parametrize(
    "temp_c, pressure_mbar, dew_point_c, expected",
    [
        (31, 1013.25, 30, 30.7),
    ]
)
def test_wet_bulb(temp_c, pressure_mbar, dew_point_c, expected):
    wet_bulb_c = wet_bulb.get_wet_bulb(temp_c, pressure_mbar, dew_point_c)

    assert wet_bulb_c == expected




