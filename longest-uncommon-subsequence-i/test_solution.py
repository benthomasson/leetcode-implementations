"""Tests for Longest Uncommon Subsequence I."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution


class TestFindLUSlength(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # LeetCode examples
    def test_example1_different_same_length(self):
        self.assertEqual(self.sol.findLUSlength("aba", "cdc"), 3)

    def test_example2_all_same_char_different(self):
        self.assertEqual(self.sol.findLUSlength("aaa", "bbb"), 3)

    def test_example3_equal_strings(self):
        self.assertEqual(self.sol.findLUSlength("aaa", "aaa"), -1)

    # Edge cases
    def test_single_char_equal(self):
        self.assertEqual(self.sol.findLUSlength("a", "a"), -1)

    def test_single_char_different(self):
        self.assertEqual(self.sol.findLUSlength("a", "b"), 1)

    def test_different_lengths(self):
        self.assertEqual(self.sol.findLUSlength("ab", "a"), 2)

    def test_different_lengths_reversed(self):
        self.assertEqual(self.sol.findLUSlength("a", "ab"), 2)

    def test_long_equal(self):
        s = "a" * 100
        self.assertEqual(self.sol.findLUSlength(s, s), -1)

    def test_long_different(self):
        self.assertEqual(self.sol.findLUSlength("a" * 100, "b" * 100), 100)


if __name__ == "__main__":
    unittest.main()
