import unittest
import task


class TestCaseConvNum(unittest.TestCase):

    def test1(self):
        # return None for an empty string?
        sample = ''
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test2(self):
        # return None for non-string types?
        sample = 1456
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test3(self):
        # return integer correctly?
        sample = '7898465321'
        expected = 7898465321
        self.assertEqual(expected, task.conv_num(sample))

    def test4(self):
        # return integer type correctly?
        sample = '1234'
        expected = int
        self.assertEqual(expected, type(task.conv_num(sample)))

    def test5(self):
        # return hex correctly?
        sample = '0xaAbBcCdDEeFf'
        expected = 187723572702975
        self.assertEqual(expected, task.conv_num(sample))

    def test6(self):
        # return float correctly?
        sample = '1256464.56'
        expected = 1256464.56
        self.assertEqual(expected, task.conv_num(sample))

    def test7(self):
        # return None for float with multiple decimal points?
        sample = '1211.13.1...'
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test8(self):
        # return float type correctly?
        sample = '1211.1'
        expected = float
        self.assertEqual(expected, type(task.conv_num(sample)))

    def test9(self):
        # return None for non-hex alphabet?
        sample = '0xaAzBp'
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test10(self):
        # return None for hex without leading '0x?
        sample = 'AABB'
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test11(self):
        # return non-positive integer correctly?
        sample = '-1234'
        expected = -1234
        self.assertEqual(expected, task.conv_num(sample))

    def test12(self):
        # return non-positive hex correctly?
        sample = '-0x12fE'
        expected = -4862
        self.assertEqual(expected, task.conv_num(sample))

    def test13(self):
        # return None for invalid hex with leading '0x'?
        sample = '0x'
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test14(self):
        # return None for invalid non-positive number '-'?
        sample = '-'
        expected = None
        self.assertEqual(expected, task.conv_num(sample))

    def test15(self):
        sample = '0'
        expected = 0
        self.assertEqual(expected, task.conv_num(sample))


class TestCaseMyDateTime(unittest.TestCase):

    def test1(self):
        date = 0
        expected = "01-01-1970"
        self.assertEqual(expected, task.my_datetime(date))

    def test2(self):
        date = 86400
        expected = "01-02-1970"
        self.assertEqual(expected, task.my_datetime(date))

    def test3(self):
        date = 364 * 86400
        expected = "12-31-1970"
        self.assertEqual(expected, task.my_datetime(date))

    def test4(self):
        date = 365 * 86400
        expected = "01-01-1971"
        self.assertEqual(expected, task.my_datetime(date))

    def test5(self):
        date = 729 * 86400
        expected = "12-31-1971"
        self.assertEqual(expected, task.my_datetime(date))

    def test6(self):
        date = 732 * 86400
        expected = "01-03-1972"
        self.assertEqual(expected, task.my_datetime(date))

    def test7(self):
        date = 7854 * 86400
        expected = "07-04-1991"
        self.assertEqual(expected, task.my_datetime(date))


class TestCaseConvEndian(unittest.TestCase):

    def test1(self):
        # checking an edge case.
        num = 0
        expected = '00'
        self.assertEqual(expected, task.conv_endian(num))

    def test2(self):
        # a small number big endian.
        num = 1
        expected = '01'
        self.assertEqual(expected, task.conv_endian(num))

    def test3(self):
        # checking if 'little' endian value passes.
        num = 1
        expected = '01'
        self.assertEqual(expected, task.conv_endian(num, 'little'))

    def test4(self):
        # checking invalid endian value returns None.
        num = 1
        expected = None
        self.assertEqual(expected, task.conv_endian(num, 'middle'))

    def test5(self):
        # a small negative number, big endian.
        num = -1
        expected = '-01'
        self.assertEqual(expected, task.conv_endian(num))

    def test6(self):
        # a random number, big endian.
        num = 79846551
        expected = '04 C2 5C 97'
        self.assertEqual(expected, task.conv_endian(num))

    def test7(self):
        # a random number, little endian.
        num = 79846551
        expected = '97 5C C2 04'
        self.assertEqual(expected, task.conv_endian(num, 'little'))

    def test8(self):
        # a random number, passing 'big' value for endian.
        num = 224885255
        expected = '0D 67 7A 07'
        self.assertEqual(expected, task.conv_endian(num, 'big'))

    def test9(self):
        # a random negative number, little endian.
        num = -224885255
        expected = '-07 7A 67 0D'
        self.assertEqual(expected, task.conv_endian(num, 'little'))

    def test10(self):
        self.assertEqual(task.conv_endian(954786, 'big'), '0E 91 A2')

    def test11(self):
        self.assertEqual(task.conv_endian(954786), '0E 91 A2')

    def test12(self):
        self.assertEqual(task.conv_endian(-954786), '-0E 91 A2')

    def test13(self):
        self.assertEqual(task.conv_endian(954786, 'little'), 'A2 91 0E')

    def test14(self):
        self.assertEqual(task.conv_endian(-954786, 'little'), '-A2 91 0E')

    def test15(self):
        self.assertEqual(task.conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E')

    def test16(self):
        self.assertIsNone(task.conv_endian(num=-954786, endian='small'))

    def test17(self):
        self.assertEqual(task.conv_endian(0), '00')

    def test18(self):
        self.assertEqual(task.conv_endian(2), '02')

    def test19(self):
        self.assertEqual(task.conv_endian(1128), '04 68')

    def test20(self):
        self.assertEqual(task.conv_endian(256), '01 00')

    def test21(self):
        self.assertEqual(task.conv_endian(4096), '10 00')

    def test22(self):
        self.assertEqual(task.conv_endian(921), '03 99')

    def test23(self):
        self.assertEqual(task.conv_endian(188), 'BC')

    def test24(self):
        self.assertEqual(task.conv_endian(100), '64')

    def test25(self):
        self.assertEqual(task.conv_endian(590), '02 4E')


if __name__ == '__main__':
    unittest.main()
