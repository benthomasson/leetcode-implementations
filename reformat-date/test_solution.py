"""Tests for LeetCode #1507: Reformat Date."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestReformatDate(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        self.assertEqual(self.s.reformatDate("20th Oct 2052"), "2052-10-20")

    def test_example_2(self):
        self.assertEqual(self.s.reformatDate("6th Jun 1933"), "1933-06-06")

    def test_example_3(self):
        self.assertEqual(self.s.reformatDate("26th May 1960"), "1960-05-26")

    def test_1st_suffix(self):
        self.assertEqual(self.s.reformatDate("1st Jan 1900"), "1900-01-01")

    def test_2nd_suffix(self):
        self.assertEqual(self.s.reformatDate("2nd Feb 2100"), "2100-02-02")

    def test_3rd_suffix(self):
        self.assertEqual(self.s.reformatDate("3rd Mar 2000"), "2000-03-03")

    def test_21st_double_digit(self):
        self.assertEqual(self.s.reformatDate("21st Dec 2020"), "2020-12-21")

    def test_31st_max_day(self):
        self.assertEqual(self.s.reformatDate("31st Jul 2050"), "2050-07-31")

    def test_single_digit_day_padding(self):
        self.assertEqual(self.s.reformatDate("9th Sep 1950"), "1950-09-09")

    def test_all_months(self):
        for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1):
            self.assertEqual(self.s.reformatDate(f"10th {m} 2000"), f"2000-{i:02d}-10")


if __name__ == "__main__":
    unittest.main()
