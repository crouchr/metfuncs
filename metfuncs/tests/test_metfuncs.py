# author : R.Crouch
# Test met functions

import pytest
import metfuncs.metfuncs as metfuncs


# ----------
@pytest.mark.parametrize(
    "mph, expected",
    [
        (0.0,  0.0),
        (1.0,  0.87),
        (2.5,  2.17),
        (10.0, 8.69),
    ]
)
def test_mph_to_knots(mph, expected):
    knots = round(metfuncs.mph_to_knots(mph),4)
    assert knots == expected


# ----------
@pytest.mark.parametrize(
    "m_per_sec, expected",
    [
        (0.0,  0.0),
        (1.0,  1.94),
        (2.5,  4.86),
        (10.0, 19.44),
    ]
)
def test_m_per_sec_to_knots(m_per_sec, expected):
    knots = round(metfuncs.m_per_sec_to_knots(m_per_sec),4)
    assert knots == expected


# ----------
@pytest.mark.parametrize(
    "kph, expected",
    [
        (0.0,  0.0),
        (1.0,  0.54),
        (2.5,  1.35),
        (10.0, 5.40),
    ]
)
def test_kph_to_knots(kph, expected):
    knots = round(metfuncs.kph_to_knots(kph),4)
    assert knots == expected


@pytest.mark.parametrize(
    "knots, expected",
    [
        (0.0,  0.0),
        (1.0,  1.85),
        (2.5,  4.63),
        (10.0, 18.52),
    ]
)
def test_knots_to_kph(knots, expected):
    kph = round(metfuncs.knots_to_kph(knots), 2)
    assert kph == expected


# ----------
@pytest.mark.parametrize(
    "kph, expected",
    [
        (0.0,  0),
        (1.0,  0),
        (2.5,  1),
        (7.1,  2),
        (15.3, 3),
        (25.3, 4),
    ]
)
def test_kph_to_beaufort(kph, expected):
    beaufort = round(metfuncs.kph_to_beaufort(kph), 4)
    assert beaufort == expected


# ----------
@pytest.mark.parametrize(
    "m_per_sec, expected",
    [
        (0.0,  0),
        (1.0,  3.60),
        (5.1, 18.36),
        (10.0, 36.00),
    ]
)
def test_kph_to_beaufort(m_per_sec, expected):
    kph = round(metfuncs.metres_per_sec_to_kph(m_per_sec), 4)
    assert kph == expected


# ----------
@pytest.mark.parametrize(
    "wind_deg, expected",
    [
        (0,  "NE"),
        (45, "NE"),
        (90, "SE"),
        (91, "SE"),
        (135, "SE"),
        (179, "SE"),
        (180, "SW"),
        (360, "NW"),
    ]
)
def test_wind_deg_to_quadrant(wind_deg, expected):
    wind_quadrant = metfuncs.wind_deg_to_quadrant(wind_deg)
    assert wind_quadrant == expected


# ----------
@pytest.mark.parametrize(
    "wind_dir, expected",
    [
        ("N",  "NE"),
    ]
)
def test_wind_dir_to_quadrant(wind_dir, expected):
    wind_quadrant = metfuncs.wind_deg_to_quadrant(wind_dir)
    assert wind_quadrant == expected
