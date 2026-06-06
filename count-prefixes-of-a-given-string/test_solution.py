"""Tests for Count Prefixes of a Given String."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution


class TestCountPrefixes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"), 3)

    def test_example2(self):
        self.assertEqual(self.sol.countPrefixes(["a", "a"], "aa"), 2)

    def test_no_match(self):
        self.assertEqual(self.sol.countPrefixes(["b", "c", "d"], "abc"), 0)

    def test_word_longer_than_s(self):
        self.assertEqual(self.sol.countPrefixes(["abcd"], "abc"), 0)

    def test_word_equals_s(self):
        self.assertEqual(self.sol.countPrefixes(["abc"], "abc"), 1)

    def test_single_char_match(self):
        self.assertEqual(self.sol.countPrefixes(["a"], "a"), 1)

    def test_all_match(self):
        self.assertEqual(self.sol.countPrefixes(["a", "ab", "abc"], "abc"), 3)

    def test_duplicates_counted(self):
        self.assertEqual(self.sol.countPrefixes(["a", "a", "a"], "abc"), 3)

    def test_empty_result_all_longer(self):
        self.assertEqual(self.sol.countPrefixes(["ab", "abc", "abcd"], "a"), 0)

    def test_single_char_s(self):
        self.assertEqual(self.sol.countPrefixes(["a", "b", "c"], "a"), 1)


if __name__ == "__main__":
    unittest.main()
