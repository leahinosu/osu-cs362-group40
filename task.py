def conv_num(num_str):
    """
    Function 1: takes string, converts to a base 10 number, and returns it

    :param str num_str: string representing a number (int, float, or hex)
    :return int result: base 10 number
    """
    result = num_str
    return result


def my_datetime(num_sec):
    """
    Function 2: takes int value that represents seconds since the epoch
    (January 1, 1970), converts it to a date, and returns it as a string

    :param int num_sec: integer representing seconds since epoch
    :return str result: date (format: MM-DD-YYYY)
    """
    result = num_sec
    return result


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
