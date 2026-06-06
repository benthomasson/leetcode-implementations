"""Tests for LeetCode 1360: Number of Days Between Two Dates."""

import sys
import unittest
from datetime import date

sys.path.insert(0, "../implementer")
from solution import Solution


class TestDaysBetweenDates(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.daysBetweenDates("2019-06-29", "2019-06-30"), 1)

    def test_example2(self):
        self.assertEqual(self.s.daysBetweenDates("2020-01-15", "2019-12-31"), 15)

    # --- Edge cases ---
    def test_same_day(self):
        self.assertEqual(self.s.daysBetweenDates("2000-01-01", "2000-01-01"), 0)

    def test_reversed_order(self):
        self.assertEqual(self.s.daysBetweenDates("2019-06-30", "2019-06-29"), 1)

    def test_leap_year_feb29(self):
        self.assertEqual(self.s.daysBetweenDates("2020-02-28", "2020-03-01"), 2)

    def test_non_leap_year_feb(self):
        self.assertEqual(self.s.daysBetweenDates("2019-02-28", "2019-03-01"), 1)

    def test_century_leap_2000(self):
        self.assertEqual(self.s.daysBetweenDates("2000-02-28", "2000-03-01"), 2)

    def test_century_non_leap_1900(self):
        self.assertEqual(self.s.daysBetweenDates("1900-02-28", "1900-03-01"), 1)

    # --- Cross-validate against stdlib datetime ---
    def test_against_stdlib(self):
        pairs = [
            ("1971-01-01", "2100-12-31"),
            ("2020-01-01", "2021-01-01"),
            ("1999-12-31", "2000-03-01"),
            ("2096-02-29", "2100-01-01"),
        ]
        for d1, d2 in pairs:
            expected = abs((date.fromisoformat(d1) - date.fromisoformat(d2)).days)
            with self.subTest(d1=d1, d2=d2):
                self.assertEqual(self.s.daysBetweenDates(d1, d2), expected)


if __name__ == "__main__":
    unittest.main()
