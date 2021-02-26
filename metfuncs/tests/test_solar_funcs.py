import pytest
import solar_funcs


@pytest.mark.parametrize(
    "lux, expected",
    [
        (1,  0.0079),
    ]
)
def test_convert_lux_to_watts(lux, expected):
    watts = solar_funcs.convert_lux_to_watts(lux)

    assert watts == expected


    # >>> map_lux_to_sky_condition(0.1)
    # 'dark'
    # >>> map_lux_to_sky_condition(8.0)
    # 'twilight'
    # >>> map_lux_to_sky_condition(100.0)
    # 'overcast'
    # >>> map_lux_to_sky_condition(10000.0)
    # 'daylight'
    # >>> map_lux_to_sky_condition(50000.0)

@pytest.mark.parametrize(
    "lux, expected",
    [
        (0.1, 'dark'),
        (8.0, 'twilight'),
        (100.0, 'overcast'),
        (10000.0, 'daylight'),
        (50000.0, 'bright sky'),
    ]
)
def test_map_lux_to_sky_condition(lux, expected):
   sky_condition = solar_funcs.map_lux_to_sky_condition(lux)

   assert sky_condition == expected
