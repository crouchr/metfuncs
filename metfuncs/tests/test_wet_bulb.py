import pytest

import wet_bulb


@pytest.mark.parametrize(
    "temp_c, pressure_mbar, rel_humidity, expected",
    [
        (31, 1013.25, 70.0, 26.6),
    ]
)
def test_wet_bulb(temp_c, pressure_mbar, rel_humidity, expected):
    wet_bulb_c = wet_bulb.get_wet_bulb(temp_c, pressure_mbar, rel_humidity)

    assert wet_bulb_c == expected




