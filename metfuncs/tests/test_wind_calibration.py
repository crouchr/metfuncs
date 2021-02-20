# author : R.Crouch
# Test okta functions

import pytest
import wind_calibration


# ----------
@pytest.mark.parametrize(
    "vane_height, expected",
    [
        (1, 1.37),
        (2, 1.29),
        (3.0, 1.22),
        (4.0, 1.18),
        (10, 1.00),
    ]
)
# vane_height is in metres
def test_calc_vane_height_to_10m_multiplier(vane_height, expected):
    wind_speed_multiplier = wind_calibration.calc_vane_height_to_10m_multiplier(vane_height)

    assert wind_speed_multiplier == expected
