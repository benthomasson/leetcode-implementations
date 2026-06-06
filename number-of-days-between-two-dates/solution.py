"""LeetCode 1360: Number of Days Between Two Dates."""

import unittest


class Solution:
    """Counts days between two YYYY-MM-DD date strings."""

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """Return the absolute number of days between two dates.

        Args:
            date1: Date string in YYYY-MM-DD format.
            date2: Date string in YYYY-MM-DD format.

        Returns:
            Absolute number of days between the two dates.
        """
        return abs(self._days_from_epoch(date1) - self._days_from_epoch(date2))

    @staticmethod
    def _is_leap(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def _days_from_epoch(date: str) -> int:
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:10])
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        total = 365 * (y - 1) + (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400
        for i in range(1, m):
            total += days_in_month[i]
        if m > 2 and Solution._is_leap(y):
            total += 1
        total += d
        return total


class TestDaysBetweenDates(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.daysBetweenDates("2019-06-29", "2019-06-30"), 1)

    def test_example2(self):
        self.assertEqual(self.s.daysBetweenDates("2020-01-15", "2019-12-31"), 15)

    def test_same_day(self):
        self.assertEqual(self.s.daysBetweenDates("2000-01-01", "2000-01-01"), 0)

    def test_cross_month(self):
        self.assertEqual(self.s.daysBetweenDates("2020-01-31", "2020-02-01"), 1)

    def test_leap_year_feb(self):
        self.assertEqual(self.s.daysBetweenDates("2020-02-28", "2020-03-01"), 2)

    def test_non_leap_year_feb(self):
        self.assertEqual(self.s.daysBetweenDates("2019-02-28", "2019-03-01"), 1)

    def test_century_non_leap(self):
        # 1900 is NOT a leap year
        self.assertEqual(self.s.daysBetweenDates("1900-02-28", "1900-03-01"), 1)

    def test_century_leap(self):
        # 2000 IS a leap year
        self.assertEqual(self.s.daysBetweenDates("2000-02-28", "2000-03-01"), 2)

    def test_full_year(self):
        self.assertEqual(self.s.daysBetweenDates("2019-01-01", "2020-01-01"), 365)

    def test_full_leap_year(self):
        self.assertEqual(self.s.daysBetweenDates("2020-01-01", "2021-01-01"), 366)

    def test_max_range(self):
        self.assertEqual(self.s.daysBetweenDates("1971-01-01", "2100-12-31"), 47481)

    def test_reversed_order(self):
        self.assertEqual(self.s.daysBetweenDates("2019-06-30", "2019-06-29"), 1)


if __name__ == "__main__":
    unittest.main()
