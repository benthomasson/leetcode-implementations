"""Tests for Check if Numbers Are Ascending in a Sentence."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestAreNumbersAscending(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---
    def test_example1_ascending(self):
        self.assertTrue(self.sol.areNumbersAscending(
            "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

    def test_example2_equal(self):
        self.assertFalse(self.sol.areNumbersAscending("hello world 5 x 5"))

    def test_example3_decrease_then_increase(self):
        self.assertFalse(self.sol.areNumbersAscending(
            "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

    # --- Edge cases ---
    def test_two_numbers_ascending(self):
        self.assertTrue(self.sol.areNumbersAscending("a 1 b 2"))

    def test_two_numbers_descending(self):
        self.assertFalse(self.sol.areNumbersAscending("a 2 b 1"))

    def test_consecutive_numbers_ascending(self):
        self.assertTrue(self.sol.areNumbersAscending("1 2 3 4 5"))

    def test_boundary_1_and_99(self):
        self.assertTrue(self.sol.areNumbersAscending("i have 1 dog and 99 cats"))

    def test_adjacent_descending(self):
        self.assertFalse(self.sol.areNumbersAscending("10 9 are numbers"))

    def test_single_digit_equal(self):
        self.assertFalse(self.sol.areNumbersAscending("x 3 y 3"))

    def test_numbers_at_start_and_end(self):
        self.assertTrue(self.sol.areNumbersAscending("1 word 50"))


if __name__ == "__main__":
    unittest.main()
