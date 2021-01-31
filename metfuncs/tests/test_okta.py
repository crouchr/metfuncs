# author : R.Crouch
# Test okta functions

import pytest
import okta_funcs


# ----------
@pytest.mark.parametrize(
    "coverage, expected_okta",
    [
        (0, 0),
        (10, 1),
        (20, 2),
        (35, 3),
        (45, 4),
        (60, 5),
        (75, 6),
        (85, 7),
        (100, 8)
    ]
)
def test_coverage_to_okta(coverage, expected_okta):
    this_okta = okta_funcs.coverage_to_okta(coverage)

    assert this_okta == expected_okta


@pytest.mark.parametrize(
    "okta, expected_text, expected_abbreviation",
    [
        (0, 'Sky Clear', 'SKC'),
        (1, 'Few', 'FEW'),
        (2, 'Few', 'FEW'),
        (3, 'Scattered', 'SCT'),
        (4, 'Scattered', 'SCT'),
        (5, 'Broken', 'BKN'),
        (6, 'Broken', 'BKN'),
        (7, 'Broken', 'BKN'),
        (8, 'Overcast', 'OVC'),
    ]
)
def test_convert_okta_to_cloud_cover(okta, expected_text, expected_abbreviation):
    cloud_coverage = okta_funcs.convert_okta_to_cloud_cover(okta)

    assert cloud_coverage[0] == expected_text
    assert cloud_coverage[1] == expected_abbreviation
