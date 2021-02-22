# https://funprojects.blog/2020/01/27/use-metpy-to-help-answer-your-kids-science-questions/
# https://unidata.github.io/MetPy/latest/userguide/startingguide.html

import metpy.calc
from metpy.units import units

# ----------------------------------------------------------------------------
# shim function as the original uses numpy arrays....
# this function takes a number of seconds to run - it is is not instantaneous
# this is the function you actually use - the others are not external facing
# >>> import metpy.calc
# >>>
# >>> pressure = [101] * units.kPa
# >>> temperature = [0.5] * units.degC
# >>> dewpoint = [-2.5] * units.degC
# >>>
# >>> metpy.calc.wet_bulb_temperature(pressure, temperature, dewpoint)
# Quantity(-0.6491265444587265, 'degree_Celsius')

def get_wet_bulb(temp_c, press_mbar, dew_point_c):
    """
    Calculate wet bulb temperature

    :param temp_c: degrees Centigrade
    :param press_mbar: Pressure mbar
    :param humidity: Relative humidity (percent)
    :return: wet bulb temperature (Centigrade)
    """
    pressure = [press_mbar] * units.kPa
    temperature = [temp_c] * units.degC
    dewpoint = [dew_point_c] * units.degC

    wet_bulb_c = metpy.calc.wet_bulb_temperature(pressure, temperature, dewpoint).magnitude
    return round(wet_bulb_c, 1)


# This came with it - not sure what it is
if __name__ == "__main__":
    wet_bulb_temp_c = get_wet_bulb(temp_c=31, press_mbar=1013.25, dew_point_c=30)
    print('wet_bulb_temp_c=' + wet_bulb_temp_c.__str__())
