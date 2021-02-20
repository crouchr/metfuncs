# See Burt page 213
import math


def calc_vane_height_to_10m_multiplier(actual_height):
    """
    Calculate factor to multiply average wind speed by to compensate for weather vane less than 10m high
    :param actual_height:  metres
    :return:
    """
    x = 0.233 + (0.656 * math.log10(actual_height + 4.75))
    multiplier = 1 / x

    return round(multiplier, 2)
