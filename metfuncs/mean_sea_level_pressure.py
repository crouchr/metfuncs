
# https://stackoverflow.com/questions/50508262/using-look-up-tables-in-python

# See Table 7.2 Burt book
# Stockcross 90m - not confirmed
# Currently using 50m to see if it lines up better with OpenWeatherAPI
# TODO : Could make more even accurate by adding interpolation
# FIXME : does not work for height = 0
# In my book, I only have data for 30 degrees so just 'guess' 40C i.e. last column
def msl_k_factor(height, temp_c):
    """
    See Burt Table 7.2 p.177
    :param height: of the site above sea level, e.g. Stockcross (metres)
    :param temp: external air temperature
    :return: correction factor
    """
    # columns are -10 0 10 20 30 degrees C
    # rows are height in metres
    press_map = {
        0:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        10:  [1.3, 1.3, 1.2, 1.2, 1.1, 1.0],
        20:  [2.6, 2.5, 2.4, 2.3, 2.3, 2.2],
        30:  [3.9, 3.8, 3.6, 3.5, 3.4, 3.3],
        40:  [5.2, 5.0, 4.8, 4.7, 4.5, 4.4],
        50:  [6.5, 6.3, 6.0, 5.8, 5.6, 5.4],
        60:  [7.8, 7.5, 7.3, 7.0, 6.8, 6.6],
        70:  [9.1, 8.8, 8.5, 8.2, 7.9, 7.6],
        80:  [10.4, 10.0, 9.7, 9.4, 9.0, 8.6],
        90:  [11.7, 11.3, 10.9, 10.5, 10.2, 9.8],
        100: [13.1, 12.6, 12.1, 11.7, 11.3, 10.8],
        110: [14.4, 13.8, 13.3, 12.9, 12.5, 11.9]
    }

    #print('\n===================')
    try:

        height_rounded = int(round(height/10)*10)
        temp_rounded = int(round(temp_c/10)*10)
        col = int((temp_rounded + 10) / 10)

        #print(f"input : height = {height}")
        #print(f"input : temp_c = {temp_c}")
        #print('-------')
        #print(f"temp_rounded = {temp_rounded}")
        #print(f"col = {col}")

        row_list = press_map[height_rounded]

        k_factor = row_list[col]

        return k_factor

    except Exception as e:
        print(f"error : msl_k_factor() for height {height}, temp_c {temp_c} failed, e={e}")
        return -999    # Don't crash


# test harness - run through reasonable ranges
if __name__ == '__main__':
    import sys

    for height in range(0, 110):
        for temp_c in range(-10, 45):
            msl = msl_k_factor(height, temp_c)
            print(f"msl_k_factor() for height {height}, temp_c {temp_c} is {msl}")
            if msl == -999:
                sys.exit("A test failed : Failure case")
