"""Tests for longestPalindrome."""

import unittest
from solution import longestPalindrome


class TestLongestPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(longestPalindrome("abccccdd"), 7)

    def test_example2(self):
        self.assertEqual(longestPalindrome("a"), 1)

    def test_all_same(self):
        self.assertEqual(longestPalindrome("aaaa"), 4)

    def test_all_pairs(self):
        self.assertEqual(longestPalindrome("aabb"), 4)

    def test_all_unique(self):
        self.assertEqual(longestPalindrome("abcdef"), 1)

    def test_case_sensitive(self):
        self.assertEqual(longestPalindrome("Aa"), 1)

    def test_mixed_case_pairs(self):
        self.assertEqual(longestPalindrome("AaAa"), 4)

    def test_single_odd(self):
        self.assertEqual(longestPalindrome("ccc"), 3)

    def test_long_string(self):
        self.assertEqual(longestPalindrome("a" * 2000), 2000)


if __name__ == "__main__":
    unittest.main()
