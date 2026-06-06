"""Tests for Largest Number After Digit Swaps by Parity."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestLargestInteger(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.largestInteger(1234), 3412)

    def test_example2(self):
        self.assertEqual(self.s.largestInteger(65875), 87655)

    def test_single_digit_odd(self):
        self.assertEqual(self.s.largestInteger(7), 7)

    def test_single_digit_even(self):
        self.assertEqual(self.s.largestInteger(2), 2)

    def test_min_input(self):
        self.assertEqual(self.s.largestInteger(1), 1)

    def test_all_even_digits(self):
        self.assertEqual(self.s.largestInteger(2468), 8642)

    def test_all_odd_digits(self):
        self.assertEqual(self.s.largestInteger(1357), 7531)

    def test_repeated_digits(self):
        self.assertEqual(self.s.largestInteger(11223), 31221)

    def test_already_largest(self):
        self.assertEqual(self.s.largestInteger(9876), 9876)

    def test_max_constraint(self):
        self.assertEqual(self.s.largestInteger(1000000000), 1000000000)


if __name__ == "__main__":
    unittest.main()
