"""Tests for Remove All Adjacent Duplicates in String."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution

import unittest


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.removeDuplicates("abbaca"), "ca")

    def test_example2(self):
        self.assertEqual(self.sol.removeDuplicates("azxxzy"), "ay")

    def test_single_char(self):
        self.assertEqual(self.sol.removeDuplicates("a"), "a")

    def test_no_duplicates(self):
        self.assertEqual(self.sol.removeDuplicates("abcdef"), "abcdef")

    def test_all_duplicates(self):
        self.assertEqual(self.sol.removeDuplicates("aabbcc"), "")

    def test_nested_duplicates(self):
        self.assertEqual(self.sol.removeDuplicates("abba"), "")

    def test_cascading_duplicates(self):
        self.assertEqual(self.sol.removeDuplicates("aabccbdd"), "")

    def test_partial_removal(self):
        self.assertEqual(self.sol.removeDuplicates("aab"), "b")

    def test_large_input(self):
        s = "ab" * 50000
        self.assertEqual(self.sol.removeDuplicates(s), s)


if __name__ == "__main__":
    unittest.main()
