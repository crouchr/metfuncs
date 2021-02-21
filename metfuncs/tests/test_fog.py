import pytest

import fog


@pytest.mark.parametrize(
    "temp_c, dew_point_c, wet_bulb_c, expected",
    [
        (1, 1, 1, True),
        (-1, -1, -1, True),
        (-1, -1, -3, False),
        (10, 20, 30, False),
    ]
)
def test_fog_1(temp_c, dew_point_c, wet_bulb_c, expected):
    is_fog = fog.fog_algo_1(temp_c, dew_point_c, wet_bulb_c)

    assert is_fog == expected
