"""Tests for count_valid_times."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import count_valid_times


class TestCountValidTimes(unittest.TestCase):
    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(count_valid_times("?5:00"), 2)

    def test_example2(self):
        self.assertEqual(count_valid_times("0?:0?"), 100)

    def test_example3(self):
        self.assertEqual(count_valid_times("??:??"), 1440)

    # --- No unknowns ---
    def test_no_unknowns(self):
        self.assertEqual(count_valid_times("12:34"), 1)

    def test_boundary_max(self):
        self.assertEqual(count_valid_times("23:59"), 1)

    # --- Single ? in each position ---
    def test_hour_tens_unknown_with_high_ones(self):
        # ?9 -> 09, 19 (not 29)
        self.assertEqual(count_valid_times("?9:00"), 2)

    def test_hour_tens_unknown_with_low_ones(self):
        # ?0 -> 00, 10, 20
        self.assertEqual(count_valid_times("?0:00"), 3)

    def test_hour_ones_unknown_with_tens_2(self):
        # 2? -> 20,21,22,23
        self.assertEqual(count_valid_times("2?:00"), 4)

    def test_minute_tens_unknown(self):
        # 00:?0 -> 00,10,20,30,40,50
        self.assertEqual(count_valid_times("00:?0"), 6)

    def test_minute_ones_unknown(self):
        self.assertEqual(count_valid_times("00:0?"), 10)


if __name__ == "__main__":
    unittest.main()
