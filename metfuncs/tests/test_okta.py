# author : R.Crouch
# Test okta functions

import pytest
import okta_funcs


# ----------
@pytest.mark.parametrize(
    "coverage, is_fog, expected_okta",
    [
        (-20, False, -1),
        (0, False, 0),
        (10, False, 1),
        (20, False, 2),
        (35, False, 3),
        (45, False, 4),
        (60, False, 5),
        (75, False, 6),
        (85, False, 7),
        (100, False, 8),
        (35, True, 9),
    ]
)
def test_coverage_to_okta(coverage, is_fog, expected_okta):
    this_okta = okta_funcs.coverage_to_okta(coverage, is_fog)

    assert this_okta == expected_okta


@pytest.mark.parametrize(
    "okta, expected_text, expected_abbreviation",
    [   (-1, 'N/A', 'N/A'),
        (0, 'Sky Clear', 'SKC'),
        (1, 'Few', 'FEW'),
        (2, 'Few', 'FEW'),
        (3, 'Scattered', 'SCT'),
        (4, 'Scattered', 'SCT'),
        (5, 'Broken', 'BKN'),
        (6, 'Broken', 'BKN'),
        (7, 'Broken', 'BKN'),
        (8, 'Overcast', 'OVC'),
        (9, 'Obstructed', 'OBS'),
    ]
)
def test_convert_okta_to_cloud_cover(okta, expected_text, expected_abbreviation):
    cloud_coverage = okta_funcs.convert_okta_to_cloud_cover(okta)

    assert cloud_coverage[0] == expected_text
    assert cloud_coverage[1] == expected_abbreviation
