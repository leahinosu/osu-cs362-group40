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

    result = ''
    temp_result = ''
    result_list = []
    neg_val = False

    # verify valid endian flag, return None if invalid
    if endian != 'big' and endian != 'little':
        return None

    # special case: input is 0
    if num == 0:
        return '00'

    # verify if result should be negative
    if num < 0:
        neg_val = True
        num = abs(num)

    # loop through and convert to hex using helper function
    while num > 0:
        temp_result = conv_endian_hex_helper(num % 16) + temp_result
        num = num // 16
        if len(temp_result) == 2:
            result_list.append(temp_result)
            temp_result = ''

    # pad extra zero on front if necessary
    if len(temp_result) > 0:
        result_list.append('0' + temp_result)

    # reverse big endian values
    if endian == 'big':
        result_list.reverse()

    # convert list to string output
    while len(result_list) > 0:
        result = result + result_list.pop(0)
        if len(result_list) > 0:
            result = result + " "

    # make negative if necessary
    if neg_val:
        return '-' + result

    return result


def conv_endian_hex_helper(num):
    """using dictionary to convert decimal int to hexadecimal string"""
    dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                  7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D',
                  14: 'E', 15: 'F', 16: '0'}
    return dec_to_hex.get(num)
