"""Tests for LeetCode 2278: Percentage of Letter in String."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution
import unittest


class TestPercentageLetter(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.percentageLetter("foobar", "o"), 33)

    def test_example2(self):
        self.assertEqual(self.sol.percentageLetter("jjjj", "k"), 0)

    def test_all_match(self):
        self.assertEqual(self.sol.percentageLetter("aaaa", "a"), 100)

    def test_no_match(self):
        self.assertEqual(self.sol.percentageLetter("abcdef", "z"), 0)

    def test_single_char_match(self):
        self.assertEqual(self.sol.percentageLetter("a", "a"), 100)

    def test_single_char_no_match(self):
        self.assertEqual(self.sol.percentageLetter("a", "b"), 0)

    def test_floor_rounding(self):
        # 1/3 = 33.33...% -> 33
        self.assertEqual(self.sol.percentageLetter("abc", "a"), 33)

    def test_floor_rounding_two_thirds(self):
        # 2/3 = 66.66...% -> 66
        self.assertEqual(self.sol.percentageLetter("aab", "a"), 66)

    def test_half(self):
        self.assertEqual(self.sol.percentageLetter("ab", "a"), 50)


if __name__ == "__main__":
    unittest.main()
