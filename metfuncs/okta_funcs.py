#
def coverage_to_okta(coverage, is_fog):
    """
    Convert cloud coverage percent to Okta
    :param coverage:
    :return:
    """
    if is_fog:
        okta = 9
    elif coverage < 0:
        okta = -1           # special case where coverage is not known e.g. in middle of night
    elif coverage == 0:
        okta = 0
    elif coverage > 0 and coverage < 18.75:
        okta = 1
    elif coverage >= 18.75 and coverage < 31.25:
        okta = 2
    elif coverage >= 31.25 and coverage < 43.75:
        okta = 3
    elif coverage >= 43.75 and coverage < 56.25:
        okta = 4
    elif coverage >= 56.25 and coverage < 68.75:
        okta = 5
    elif coverage >= 68.75 and coverage < 81.25:
        okta = 6
    elif coverage >= 81.25 and coverage < 100:
        okta = 7
    elif coverage == 100:
        okta = 8

    return okta

# -1 = unable to determine the numercial okta value
# 9 = fog
def convert_okta_to_cloud_cover(okta):
    """
    Convert Okta to Cloud Cover Text
    :param okta:
    :return:
    """

    if okta == -1:
        cloud_cover = ('N/A', 'N/A')
    elif okta == 0:
        cloud_cover = ('Sky Clear', 'SKC')
    elif okta == 1 or okta == 2:
        cloud_cover = ('Few', 'FEW')
    elif okta == 3 or okta == 4:
        cloud_cover = ('Scattered', 'SCT')
    elif okta == 5 or okta == 6 or okta == 7:
        cloud_cover = ('Broken', 'BKN')
    elif okta == 8:
        cloud_cover = ('Overcast', 'OVC')
    elif okta == 9:
        cloud_cover = ('Obfuscated', 'OBS')     # I completely made these up

    return cloud_cover
