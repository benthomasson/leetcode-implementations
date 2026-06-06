"""Tests for Latest Time by Replacing Hidden Digits."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestMaximumTime(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.maximumTime("2?:?0"), "23:50")

    def test_example2(self):
        self.assertEqual(self.s.maximumTime("0?:3?"), "09:39")

    def test_example3(self):
        self.assertEqual(self.s.maximumTime("1?:22"), "19:22")

    # --- All / no hidden ---
    def test_all_hidden(self):
        self.assertEqual(self.s.maximumTime("??:??"), "23:59")

    def test_no_hidden(self):
        self.assertEqual(self.s.maximumTime("12:34"), "12:34")

    # --- Hour digit interactions ---
    def test_h1_with_h2_large(self):
        # h2=4 means h1 can't be 2 (would give 24), so h1=1
        self.assertEqual(self.s.maximumTime("?4:00"), "14:00")

    def test_h1_with_h2_small(self):
        # h2=3 allows h1=2 (gives 23)
        self.assertEqual(self.s.maximumTime("?3:00"), "23:00")

    def test_h2_when_h1_is_2(self):
        # h1=2 limits h2 to max 3
        self.assertEqual(self.s.maximumTime("2?:00"), "23:00")

    def test_h2_when_h1_is_1(self):
        # h1=1 allows h2 up to 9
        self.assertEqual(self.s.maximumTime("1?:00"), "19:00")

    # --- Boundary values ---
    def test_midnight(self):
        self.assertEqual(self.s.maximumTime("00:00"), "00:00")

    def test_max_time(self):
        self.assertEqual(self.s.maximumTime("23:59"), "23:59")


if __name__ == "__main__":
    unittest.main()
