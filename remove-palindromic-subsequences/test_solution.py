"""Tests for Remove Palindromic Subsequences."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import countStrings


class TestCountStrings(unittest.TestCase):
    # LeetCode examples
    def test_example1_palindrome(self):
        self.assertEqual(countStrings("ababa"), 1)

    def test_example2_not_palindrome(self):
        self.assertEqual(countStrings("abb"), 2)

    def test_example3_not_palindrome(self):
        self.assertEqual(countStrings("baabb"), 2)

    # Edge cases
    def test_empty_string(self):
        self.assertEqual(countStrings(""), 0)

    def test_single_a(self):
        self.assertEqual(countStrings("a"), 1)

    def test_single_b(self):
        self.assertEqual(countStrings("b"), 1)

    def test_two_same(self):
        self.assertEqual(countStrings("aa"), 1)

    def test_two_different(self):
        self.assertEqual(countStrings("ab"), 2)

    def test_all_same_long(self):
        self.assertEqual(countStrings("a" * 1000), 1)

    def test_non_palindrome_long(self):
        self.assertEqual(countStrings("ab" * 500), 2)


if __name__ == "__main__":
    unittest.main()
