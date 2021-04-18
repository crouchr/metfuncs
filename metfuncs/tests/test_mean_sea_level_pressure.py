import pytest

import mean_sea_level_pressure


@pytest.mark.parametrize(
    "height, temp_c, expected",
    [
        (90, -8, 11.7),
        (90, -2, 11.3),
        (90, 8, 10.9),
        (90, 18, 10.5),
        (90, 28, 10.2),
    ]
)
def test_fog_1(height, temp_c, expected):
    k_factor = mean_sea_level_pressure.msl_k_factor(height, temp_c)

    assert k_factor == expected
