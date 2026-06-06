"""Tests for most_frequent_even solution."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import most_frequent_even


class TestMostFrequentEven(unittest.TestCase):
    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(most_frequent_even([0, 1, 2, 2, 4, 4, 1]), 2)

    def test_example2(self):
        self.assertEqual(most_frequent_even([4, 4, 4, 9, 2, 4]), 4)

    def test_example3_all_odd(self):
        self.assertEqual(most_frequent_even([29, 47, 21, 41, 13, 37, 25, 7]), -1)

    # --- Edge cases ---
    def test_single_even(self):
        self.assertEqual(most_frequent_even([2]), 2)

    def test_single_odd(self):
        self.assertEqual(most_frequent_even([3]), -1)

    def test_zero(self):
        self.assertEqual(most_frequent_even([0]), 0)

    def test_tie_returns_smallest(self):
        self.assertEqual(most_frequent_even([4, 2, 4, 2]), 2)

    def test_clear_winner(self):
        self.assertEqual(most_frequent_even([2, 2, 2, 4]), 2)

    def test_large_values(self):
        self.assertEqual(most_frequent_even([100000, 100000, 99999]), 100000)


if __name__ == "__main__":
    unittest.main()
