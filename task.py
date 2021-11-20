def conv_num(num_str):
    """
    Function 1: takes string, converts to a base 10 number, and returns it

    :param str num_str: string representing a number (int, float, or hex)
    :return int result: base 10 number
    """

    STR_MAPPING = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
                   'd': 13, 'e': 14, 'f': 15}
    HEX_ALPHA = ['a', 'b', 'c', 'd', 'e', 'f']

    # check invalid inputs
    if num_str == '':
        return
    if type(num_str) != str:
        return

    result = 0
    base = 10

    # check if non-positive
    is_neg = False
    if '-' in num_str:
        is_neg = True
        num_str = num_str[1:]

    # check if hex
    is_hex = False
    if len(num_str) > 2 and num_str[:2].lower() == '0x':
        is_hex = True
        num_str = num_str[2:]
        base = 16

    multiplier = len(num_str) - 1
    is_float = False

    # check if valid input
    if multiplier < 1:
        return

    for s in num_str:
        # check float
        if s == '.' and not is_float:
            is_float = True
            result //= 10**(multiplier + 1)
            multiplier = -1
            continue
        # check multiple decimal points
        if s == '.' and is_float:
            return
        # check non-mapping values
        if s.lower() not in STR_MAPPING:
            return
        # check hex without leading '0x'
        if not is_hex and s.lower() in HEX_ALPHA:
            return

        result += STR_MAPPING[s.lower()] * base**multiplier
        multiplier -= 1

    if is_neg:
        result *= -1

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
