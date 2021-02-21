# algorithms for predicting fog
# find the range that contains all three values and it must be less than a threshold I can adjust
# This will work with data calculated with an AWS
def fog_algo_1(temp_c, dew_point_c, wet_bulb_c, wind_knots_2m, permitted_range=1.0):
    """

    :param temp_c:
    :param dew_point_c:
    :param wet_bulb_c:
    :param wind_knots_2m: Wind speed at 2m high (not 10m)
    :return:
    """

    # fog won't form if wind speed is too high
    if wind_knots_2m >= 2.0:
        return False

    temps = [temp_c, dew_point_c, wet_bulb_c]

    max_temp = max(temps)
    min_temp = min(temps)

    temp_range = max_temp - min_temp

    if temp_range <= permitted_range:
        return True
    else:
        return False


# This will work with data calculated with an AWS
def fog_algo_2(temp_c, dew_point_c, wind_knots_2m):
    """

    :param temp_c:
    :param dew_point_c:
    :param wind_knots_2m:
    :return:
    """

    # fog won't form if wind speed is too high
    if wind_knots_2m >= 2.0:
        return False

    if abs(temp_c - dew_point_c) < 2.5 :
        return True
    else:
        return False

