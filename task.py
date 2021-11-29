import math


def conv_num(num_str):
    """
    Function 1: takes string, converts to a base 10 number, and returns it

    :param str num_str: string representing a number (int, float, or hex)
    :return int result: base 10 number
    """

    if num_str == '' or type(num_str) != str:
        return

    return conv_hex(num_str) if '0x' in num_str.lower() else conv_dec(num_str)


def conv_hex(num_str):
    """
    Convert a hex-string to an integer. Invalid input returns None.
    :param str num_str: a string represents a hex.
    :return int result: base 10 number.
    """

    str_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
                   'd': 13, 'e': 14, 'f': 15}

    index = 3 if num_str[0] == '-' else 2  # check the start index

    result = 0
    multiplier = len(num_str) - (index + 1)
    if multiplier < 0:
        return

    for s in num_str[index:]:
        if s.lower() not in str_mapping:
            return
        result += str_mapping[s.lower()] * (16**multiplier)
        multiplier -= 1

    return result if num_str[0] != '-' else -result


def conv_dec(num_str):
    """
    Convert a decimal-string to a decimal. Invalid input returns None.
    :param str num_str: a string represents a decimal.
    :return int, float result: base 10 number.
    """

    str_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, 'a': 10}

    index = 1 if num_str[0] == '-' else 0  # check the start index

    result = 0
    multiplier = len(num_str) - (index + 1)
    if multiplier < 0:
        return

    is_float = False
    for s in num_str[index:]:
        if s == '.' and not is_float:
            is_float = True
            result //= 10 ** (multiplier + 1)
            multiplier = -1
            continue
        if s.lower() not in str_mapping:
            return
        result += str_mapping[s.lower()] * (10**multiplier)
        multiplier -= 1

    return result if num_str[0] != '-' else -result


def day_helper(remaining_days, current):
    if current % 4 == 0:
        if remaining_days < 32:
            month = '01'
            day = remaining_days - 0
        if 31 < remaining_days < 61:
            month = '02'
            day = remaining_days - 31
        if 60 < remaining_days < 92:
            month = '03'
            day = remaining_days - 60
        if 91 < remaining_days < 122:
            month = '04'
            day = remaining_days - 91
        if 121 < remaining_days < 153:
            month = '05'
            day = remaining_days - 121
        if 152 < remaining_days < 183:
            month = '06'
            day = remaining_days - 152
        if 182 < remaining_days < 214:
            month = '07'
            day = remaining_days - 182
        if 213 < remaining_days < 245:
            month = '08'
            day = remaining_days - 213
        if 244 < remaining_days < 275:
            month = '09'
            day = remaining_days - 244
        if 274 < remaining_days < 306:
            month = '10'
            day = remaining_days - 274
        if 305 < remaining_days < 336:
            month = '11'
            day = remaining_days - 303
        if 335 < remaining_days < 367:
            month = '12'
            day = remaining_days - 335
    else:
        if remaining_days < 32:
            month = '01'
            day = remaining_days - 0
        if 31 < remaining_days < 60:
            month = '02'
            day = remaining_days - 30
        if 59 < remaining_days < 91:
            month = '03'
            day = remaining_days - 59
        if 90 < remaining_days < 121:
            month = '04'
            day = remaining_days - 90
        if 120 < remaining_days < 152:
            month = '05'
            day = remaining_days - 120
        if 151 < remaining_days < 182:
            month = '06'
            day = remaining_days - 151
        if 181 < remaining_days < 213:
            month = '07'
            day = remaining_days - 181
        if 212 < remaining_days < 244:
            month = '08'
            day = remaining_days - 212
        if 243 < remaining_days < 274:
            month = '09'
            day = remaining_days - 243
        if 273 < remaining_days < 305:
            month = '10'
            day = remaining_days - 273
        if 304 < remaining_days < 335:
            month = '11'
            day = remaining_days - 304
        if 334 < remaining_days < 366:
            month = '12'
            day = remaining_days - 334

    day += 1

    if day < 10:
        day = '0' + str(day)

    result = str(month) + "-" + str(day) + "-" + str(current)

    return result


def my_datetime(num_sec):
    """
    Function 2: takes int value that represents seconds since the epoch
    (January 1, 1970), converts it to a date, and returns it as a string

    :param int num_sec: integer representing seconds since epoch
    :return str result: date (format: MM-DD-YYYY)
    """

    result = num_sec

    epoch = 1970
    num_minutes = num_sec / 60
    num_hours = num_minutes / 60
    num_days = num_hours / 24
    holder = int(math.floor(num_days))
    current = epoch
    for i in range(1, holder):
        if holder < 366 and (current + 1) % 4 == 0:
            break
        if holder < 365:
            break
        elif (current % 4) != 0:
            current = current + 1
            holder = holder - 365
        elif (current % 4) == 0:
            current = current + 1
            holder = holder - 366
    actual_year = current
    remaining_days = holder
    # if remaining_days == 0:
    #     remaining_days = remaining_days + 1
    # print(current)
    return day_helper(remaining_days, current)


def conv_endian(num, endian='big'):
    """
    Function 3: takes an integer value and converts to a hexadecimal number,
    endian type is determined by the endian flag.

    :param int num: integer value
    :param str endian: big/little endian flag
    :return str result: hexadecimal number with proper endian
    """
    result = num
    return result, endian
