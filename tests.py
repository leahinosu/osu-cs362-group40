import unittest
import task
from task import my_datetime


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test16(self):
        date = 123456789
        expected = "11-29-1973"
        self.assertEqual(expected, my_datetime(date))

    def test17(self):
        date = 0
        expected = "01-1-1970"
        self.assertEqual(expected, my_datetime(date))


if __name__ == '__main__':
    unittest.main()
