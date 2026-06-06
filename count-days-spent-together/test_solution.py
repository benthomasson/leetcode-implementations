"""Tests for count-days-spent-together solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import days_together, _date_to_day


class TestDateToDay(unittest.TestCase):
    """Verify the helper converts dates correctly."""

    def test_jan_1(self):
        self.assertEqual(_date_to_day("01-01"), 1)

    def test_dec_31(self):
        self.assertEqual(_date_to_day("12-31"), 365)

    def test_feb_28(self):
        self.assertEqual(_date_to_day("02-28"), 59)


class TestDaysTogether(unittest.TestCase):

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(days_together("08-15", "08-18", "08-16", "08-19"), 3)

    def test_example2(self):
        self.assertEqual(days_together("10-01", "10-31", "11-01", "12-31"), 0)

    # --- Edge cases ---
    def test_same_single_day(self):
        self.assertEqual(days_together("07-04", "07-04", "07-04", "07-04"), 1)

    def test_identical_ranges(self):
        self.assertEqual(days_together("03-01", "03-10", "03-01", "03-10"), 10)

    def test_no_overlap_adjacent(self):
        self.assertEqual(days_together("01-01", "01-31", "02-01", "02-28"), 0)

    def test_single_day_boundary_overlap(self):
        self.assertEqual(days_together("01-01", "01-05", "01-05", "01-10"), 1)

    def test_containment(self):
        self.assertEqual(days_together("01-01", "12-31", "06-01", "06-30"), 30)

    def test_full_year_both(self):
        self.assertEqual(days_together("01-01", "12-31", "01-01", "12-31"), 365)

    def test_cross_month(self):
        self.assertEqual(days_together("01-28", "02-05", "02-01", "02-10"), 5)

    def test_bob_before_alice(self):
        self.assertEqual(days_together("06-01", "06-30", "03-01", "03-31"), 0)


if __name__ == "__main__":
    unittest.main()
