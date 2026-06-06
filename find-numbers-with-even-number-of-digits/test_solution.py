"""Tests for Find Numbers with Even Number of Digits."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution


class TestFindNumbers(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findNumbers([12, 345, 2, 6, 7896]), 2)

    def test_example2(self):
        self.assertEqual(self.s.findNumbers([555, 901, 482, 1771]), 1)

    def test_single_digit(self):
        self.assertEqual(self.s.findNumbers([5]), 0)

    def test_two_digits(self):
        self.assertEqual(self.s.findNumbers([10]), 1)

    def test_all_even_digit_counts(self):
        self.assertEqual(self.s.findNumbers([12, 34, 1771]), 3)

    def test_all_odd_digit_counts(self):
        self.assertEqual(self.s.findNumbers([1, 100, 10000]), 0)

    def test_max_constraint(self):
        # 100000 = 6 digits (even)
        self.assertEqual(self.s.findNumbers([100000]), 1)

    def test_mixed_digit_lengths(self):
        # 1-digit(odd), 2-digit(even), 3-digit(odd), 4-digit(even), 5-digit(odd), 6-digit(even)
        self.assertEqual(self.s.findNumbers([1, 10, 100, 1000, 10000, 100000]), 3)


if __name__ == "__main__":
    unittest.main()
