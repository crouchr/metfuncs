# algorithms for predicting fog
# find the range that contains all three values and it must be less than a threshold I can adjust
def fog_algo_1(temp_c, dew_point_c, wet_bulb_c, permitted_range=1.0):
    """

    :param temp_c:
    :param dew_point_c:
    :param wet_bulb_c:
    :return:
    """
    temps = [temp_c, dew_point_c, wet_bulb_c]

    max_temp = max(temps)
    min_temp = min(temps)

    temp_range = max_temp - min_temp

    if temp_range <= permitted_range:
        return True
    else:
        return False
