# https://realpython.com/python-datetime/#working-with-time-zones

import datetime
from dateutil import tz
import pysolar


def calc_altitude(lat, lon):
    date = datetime.datetime.now(tz=tz.UTC)
    altitude = pysolar.solar.get_altitude(lat, lon, date)

    if altitude < 0:
        altitude = 0

    return round(altitude, 3)


def calc_azimuth(lat, lon):
    """
    0 degrees = North
    :param lat:
    :param lon:
    :return:
    """
    date = datetime.datetime.now(tz=tz.UTC)
    azimuth = pysolar.solar.get_azimuth(lat, lon, date)

    if azimuth < 0:
        azimuth = 0

    return round(azimuth, 1)


def get_solar_radiation_theoretical(altitude_deg):
    date = datetime.datetime.now(tz=tz.UTC)
    if altitude_deg <= 0:
        solar_radiation = 0.0
    else:
        solar_radiation = pysolar.solar.radiation.get_radiation_direct(date, altitude_deg=altitude_deg)

    return round(solar_radiation, 1)


def calc_cloud_coverage(solar_rad_actual, solar_rad_theoretical):
    """

    :param solar_rad_actual:
    :param solar_rad_theoretical:
    :return:
    """

    if solar_rad_theoretical < 10.0:
        return -10          # make it obvious we are in this case

    solar_fraction = solar_rad_actual / solar_rad_theoretical

    cloud_coverage = 100 * (1-solar_fraction)

    return int(cloud_coverage)


if __name__ == '__main__':
    lat = 51.4151
    lon = -1.3776

    azimuth = calc_azimuth(lat, lon)
    print(azimuth)

    altitude = calc_altitude(lat, lon)
    print(altitude)

    solar_radiation_theoretical = get_solar_radiation_theoretical(altitude)
    print(solar_radiation_theoretical)

    cloud_coverage = calc_cloud_coverage(20, 100)
    print(cloud_coverage)
