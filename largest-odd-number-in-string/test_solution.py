"""Tests for largest_odd_number."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import largest_odd_number


class TestLargestOddNumber(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(largest_odd_number("52"), "5")

    def test_example2(self):
        self.assertEqual(largest_odd_number("4206"), "")

    def test_example3(self):
        self.assertEqual(largest_odd_number("35427"), "35427")

    # Edge cases
    def test_single_odd_digit(self):
        self.assertEqual(largest_odd_number("9"), "9")

    def test_single_even_digit(self):
        self.assertEqual(largest_odd_number("8"), "")

    def test_odd_at_end(self):
        self.assertEqual(largest_odd_number("2461"), "2461")

    def test_odd_only_at_start(self):
        self.assertEqual(largest_odd_number("1248"), "1")

    def test_all_even_digits(self):
        self.assertEqual(largest_odd_number("248060"), "")

    def test_all_odd_digits(self):
        self.assertEqual(largest_odd_number("13579"), "13579")

    def test_large_input(self):
        self.assertEqual(largest_odd_number("2" * 100000), "")


if __name__ == "__main__":
    unittest.main()
