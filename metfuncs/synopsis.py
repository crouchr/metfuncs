# https://artefacts.ceda.ac.uk/badc_datadocs/surface/code.html
import fog
import solar_funcs


# Rain and drizzle are the only forms of liquid precipitation.
# Rain is classified as light, meaning rain falling at a rate between a trace and 0.10 inch per hour;
# moderate, 0.11 to 0.30 inch per hour;
# heavy, more than 0.30 inch per hour.28 Sept 2018
def get_synopsis(temp_c, wet_bulb_c, dew_point_c, rain_rate, wind_knots_2m, solar):
    """
    Calculate the WMO 4680 current weather code and text

    :param temp_c:
    :param wet_bulb_c:
    :param dew_point_c:
    :param rain_rate:
    :param wind_knots_2m:
    :return:
    """

    is_foggy = fog.fog_algo_1(temp_c, dew_point_c, wet_bulb_c, wind_knots_2m, solar)

    if rain_rate > 0.0 and rain_rate < 2.54:
        rain = 'slight'
    elif rain_rate >= 2.54 and rain_rate < 7.62:
        rain = 'moderate'
    elif rain_rate >= 7.62:
        rain = 'heavy'
    else:
        rain = 'none'

    if rain == 'slight':
        if temp_c > 0.0:
            return 61, "Rain, not freezing, slight"
        else:
            return 64, "Rain, freezing, slight"
    elif rain == 'moderate':
        if temp_c > 0.0:
            return 62, "Rain, not freezing, moderate"
        else:
            return 65, "Rain, freezing, moderate"
    elif rain == 'heavy':
        if temp_c > 0.0:
            return 63, "Rain, not freezing, heavy"
        else:
            return 66, "Rain, freezing, heavy"

    if is_foggy:
        if temp_c < 0.0:
            return 31, 'Fog or ice fog in patches'
        else:
            return 30, "FOG"

    # wait until I have built ultrasonic snow detector
    # if temp_c < 3.0:
    #     return 70, "SNOW"

    # return 0, 'No significant weather observed' # this is official one but make shorter for .tsv file
    return 0, '-None-'


# Rain is handled in the WMO Synopsis
def get_additional_synopsis(temp_c, wet_bulb_c, dew_point_c, beaufort, lux):
    """
    Return non-WMO additional synopsis information
    :param temp_c:
    :param wet_bulb_c:
    :param dew_point_c:
    :param wind_knots_2m:
    :param lux:
    :return:
    """

    sky_condition = solar_funcs.map_lux_to_sky_condition(lux)
    wind_condition = map_wind_speed_to_condition(beaufort)
    # temp_condition =

    synopsis_text = sky_condition
    synopsis_text += ', ' + wind_condition
    # synopsis_text += ', ' + temp_condition

    return synopsis_text


def map_wind_speed_to_condition(beaufort):
    beaufort_map = {
        '0' : 'calm',
        '1' : 'Light air',

    }