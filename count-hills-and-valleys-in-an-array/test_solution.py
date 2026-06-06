"""Tests for Count Hills and Valleys in an Array."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import count_hills_and_valleys


class TestCountHillsAndValleys(unittest.TestCase):
    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(count_hills_and_valleys([2, 4, 1, 1, 6, 5]), 3)

    def test_example2(self):
        self.assertEqual(count_hills_and_valleys([6, 6, 5, 5, 4, 1]), 0)

    # --- Edge cases ---
    def test_all_same(self):
        self.assertEqual(count_hills_and_valleys([5, 5, 5]), 0)

    def test_minimum_length_hill(self):
        self.assertEqual(count_hills_and_valleys([1, 3, 1]), 1)

    def test_minimum_length_valley(self):
        self.assertEqual(count_hills_and_valleys([3, 1, 3]), 1)

    def test_monotonic_increasing(self):
        self.assertEqual(count_hills_and_valleys([1, 2, 3, 4, 5]), 0)

    def test_monotonic_decreasing(self):
        self.assertEqual(count_hills_and_valleys([5, 4, 3, 2, 1]), 0)

    def test_plateau_hill(self):
        self.assertEqual(count_hills_and_valleys([1, 5, 5, 5, 1]), 1)

    def test_alternating(self):
        self.assertEqual(count_hills_and_valleys([1, 3, 1, 3, 1]), 3)

    def test_plateau_valley(self):
        self.assertEqual(count_hills_and_valleys([5, 1, 1, 1, 5]), 1)


if __name__ == "__main__":
    unittest.main()
