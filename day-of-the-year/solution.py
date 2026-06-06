"""Day of the Year - LeetCode solution."""

import unittest

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year.

    Args:
        year: The year to check.

    Returns:
        True if the year is a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def dayOfYear(date: str) -> int:
    """Return the day number of the year for a given date.

    Args:
        date: Date string formatted as YYYY-MM-DD.

    Returns:
        The 1-indexed day number of the year.
    """
    year, month, day = map(int, date.split("-"))
    result = sum(DAYS_IN_MONTH[:month - 1]) + day
    if is_leap_year(year) and month > 2:
        result += 1
    return result


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

    def test_feb28_leap(self):
        self.assertEqual(dayOfYear("2016-02-28"), 59)

    def test_feb29_leap(self):
        self.assertEqual(dayOfYear("2016-02-29"), 60)

    def test_mar1_leap(self):
        self.assertEqual(dayOfYear("2016-03-01"), 61)

    def test_mar1_non_leap(self):
        self.assertEqual(dayOfYear("2019-03-01"), 60)

    def test_1900_not_leap(self):
        self.assertEqual(dayOfYear("1900-12-31"), 365)

    def test_2000_leap(self):
        self.assertEqual(dayOfYear("2000-12-31"), 366)

    def test_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2016))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2019))


if __name__ == "__main__":
    unittest.main()
