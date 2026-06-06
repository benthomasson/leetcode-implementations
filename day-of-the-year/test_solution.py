"""Tests for Day of the Year solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import dayOfYear, is_leap_year


class TestDayOfYear(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(dayOfYear("2019-01-09"), 9)

    def test_example2(self):
        self.assertEqual(dayOfYear("2019-02-10"), 41)

    def test_jan1(self):
        self.assertEqual(dayOfYear("2019-01-01"), 1)

    def test_dec31_non_leap(self):
        self.assertEqual(dayOfYear("2019-12-31"), 365)

    def test_dec31_leap(self):
        self.assertEqual(dayOfYear("2016-12-31"), 366)

    def test_leap_boundary_feb29(self):
        self.assertEqual(dayOfYear("2016-02-29"), 60)

    def test_1900_not_leap(self):
        self.assertEqual(dayOfYear("1900-12-31"), 365)

    def test_2000_leap(self):
        self.assertEqual(dayOfYear("2000-12-31"), 366)

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2016))
        self.assertFalse(is_leap_year(2019))


if __name__ == "__main__":
    unittest.main()
