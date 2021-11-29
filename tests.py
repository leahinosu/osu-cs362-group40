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


class TestCaseConvEndian(unittest.TestCase):

    def test01(self):
        self.assertEqual(task.conv_endian(954786, 'big'), '0E 91 A2')

    def test02(self):
        self.assertEqual(task.conv_endian(954786), '0E 91 A2')

    def test03(self):
        self.assertEqual(task.conv_endian(-954786), '-0E 91 A2')

    def test04(self):
        self.assertEqual(task.conv_endian(954786, 'little'), 'A2 91 0E')

    def test05(self):
        self.assertEqual(task.conv_endian(-954786, 'little'), '-A2 91 0E')

    def test06(self):
        self.assertEqual(task.conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E')

    def test07(self):
        self.assertIsNone(task.conv_endian(num=-954786, endian='small'))

    def test08(self):
        self.assertEqual(task.conv_endian(0), '00')

    def test09(self):
        self.assertEqual(task.conv_endian(2), '02')

    def test10(self):
        self.assertEqual(task.conv_endian(1128), '04 68')

    def test11(self):
        self.assertEqual(task.conv_endian(256), '01 00')

    def test12(self):
        self.assertEqual(task.conv_endian(4096), '10 00')

    def test13(self):
        self.assertEqual(task.conv_endian(921), '03 99')

    def test14(self):
        self.assertEqual(task.conv_endian(188), 'BC')

    def test15(self):
        self.assertEqual(task.conv_endian(100), '64')

    def test16(self):
        self.assertEqual(task.conv_endian(590), '02 4E')


if __name__ == '__main__':
    unittest.main()
