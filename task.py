# function 1 =================================================================
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
    Helper function for function 1, num_str.
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
    Helper function for function 1, num_str.
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


# function 2 =================================================================
def my_datetime(num_sec):
    """
    Function 2: takes int value that represents seconds since the epoch
    (January 1, 1970), converts it to a date, and returns it as a string

    :param int num_sec: integer representing seconds since epoch
    :return str result: date (format: MM-DD-YYYY)
    """
    num_minutes = num_sec // 60
    num_hours = num_minutes // 60
    num_days = num_hours // 24

    year, remaining_days, is_leap = get_year(num_days)

    month, day = get_month_day(remaining_days, is_leap)

    return conv_date_to_str(year, month, day)


def get_year(holder: int) -> tuple:
    """
    Helper function for function 2, my_datetime.
    Calculate and return the year based on the given number of days.
    :param int holder: number of days.
    :return tuple (current: int, holder: int, is_leap: bool):
        current: current year
        holder: remaining days
        is_leap: True if the current year is a leap year.
    """
    epoch = 1970
    current = epoch
    is_leap = False
    while True:
        if current % 4 == 0 and holder < 366:
            is_leap = True
            break
        if holder < 365:
            break
        elif (current % 4) != 0:
            current = current + 1
            holder = holder - 365
        elif (current % 4) == 0:
            current = current + 1
            holder = holder - 366
    return current, holder, is_leap


def get_month_day(remaining_days: int, is_leap: bool) -> tuple:
    """
    Helper function for function 2, my_datetime.
    Calculate and return the month and the day based on the given
    remaining days.
    :param int remaining_days: number of days.
    :param bool is_leap: True if the current year is a leap year.
        Otherwise, false.
    :return tuple (month: int, day: int):
    """
    # days per month starting from January.
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap:
        month_day[1] = 29

    index = 0
    month = 1
    while remaining_days >= month_day[index]:
        remaining_days -= month_day[index]
        index += 1
        month = index + 1

    return month, remaining_days + 1


def conv_date_to_str(year: int, month: int, day: int) -> str:
    """
    Helper function for function 2, my_datetime.
    Convert year, month, and day to a string in format 'mm-dd-yyyy'.
    :param year:
    :param month:
    :param day:
    :return str:
    """
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    temp_list = [str(month), str(day), str(year)]
    return '-'.join(temp_list)


# function 3 =================================================================
def conv_endian(num, endian='big'):
    """
    Function 3: takes an integer value and converts to a hexadecimal number,
    endian type is determined by the endian flag.

    :param int num: integer value
    :param str endian: big/little endian flag
    :return str result: hexadecimal number with proper endian
    """
    possible_inputs = ['big', 'little']
    if endian not in possible_inputs:
        return

    hex_str = format_hex_str(conv_dec_to_hex(num), endian)
    return add_neg(hex_str) if num < 0 else hex_str


def conv_dec_to_hex(num: int) -> str:
    """
    Helper function for function 3, conv_endian.
    Convert an integer to a hex and then return the result in string.
    If the given integer is negative, convert it to positive.
    Add '0' in front if length of the result string is not even.
    :param int num: an integer
    :return str: hex of num.
    """
    result = ''
    num_mapping = [str(i) for i in range(10)]
    char_mapping = [chr(i) for i in range(65, 71)]  # 'A' to 'F'
    hex_mapping = num_mapping + char_mapping

    if num < 0:
        num = abs(num)

    while num:
        result = hex_mapping[num % 16] + result
        num //= 16

    if result == '':
        result = '0'

    if len(result) % 2 != 0:
        result = '0' + result

    return result


def format_hex_str(hex_str: str, endian='big') -> str:
    """
    Helper function for function 3, conv_endian.
    Format hex_str to have a space per byte and to have 2 characters per byte.
    It also arrange each bytes based on the given endian value.
    Default endian is big. It assumes hex_str represents a positive hex.
    :param str hex_str: string represents a hex
    :param endian: endian either 'big' or 'little'
    :return str:
    """
    temp_list = []
    result = ''
    is_second = False
    for c in hex_str:
        result = result + c
        if is_second:
            temp_list.append(result)
            result = ''
        is_second = not is_second

    if endian == 'little':
        temp_list = temp_list[:: -1]

    return ' '.join(temp_list)


def add_neg(hex_str):
    """
    Helper function for function 3, conv_endian.
    Add negative sign to the given string.
    :param hex_str: string represents a hex
    :return str:
    """
    return '-' + hex_str
