# This is a copy of the file from metfuncs artifacts - i just copied for speed's sake

# https://funprojects.blog/2020/01/27/use-metpy-to-help-answer-your-kids-science-questions/
# https://unidata.github.io/MetPy/latest/userguide/startingguide.html

import metpy.calc
from metpy.units import units


def get_dew_point(temp_c, humidity_percent):
    """

    :param temp_c:
    :param humidity:
    :return:
    """

    humidity = humidity_percent / 100
    temperature = [temp_c] * units.degC
    dew_point_c = metpy.calc.dewpoint_from_relative_humidity(temperature, humidity).magnitude[0]

    return round(dew_point_c, 1)





# Test code
if __name__ == "__main__":

    temp_c = 25.9
    humidity_percent = 67

    dew_point_c = get_dew_point(temp_c, humidity_percent)
    print('dew_point_c=' + dew_point_c.__str__())