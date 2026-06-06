"""Tests for LeetCode 1370: Increasing Decreasing String."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestSortString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.sortString("aaaabbbbcccc"), "abccbaabccba")

    def test_example2(self):
        self.assertEqual(self.sol.sortString("rat"), "art")

    def test_single_char(self):
        self.assertEqual(self.sol.sortString("a"), "a")

    def test_all_same_char(self):
        self.assertEqual(self.sol.sortString("aaaa"), "aaaa")

    def test_two_distinct(self):
        # a=2, b=2 -> forward: ab, backward: ba -> "abba"
        self.assertEqual(self.sol.sortString("aabb"), "abba")

    def test_full_alphabet(self):
        s = "zyxwvutsrqponmlkjihgfedcba"
        self.assertEqual(self.sol.sortString(s), "abcdefghijklmnopqrstuvwxyz")

    def test_output_length_matches_input(self):
        s = "leetcode"
        result = self.sol.sortString(s)
        self.assertEqual(len(result), len(s))
        self.assertEqual(sorted(result), sorted(s))

    def test_uneven_frequencies(self):
        # a=3, b=1 -> fwd: ab, bwd: a, fwd: a -> "abaa"
        self.assertEqual(self.sol.sortString("aaab"), "abaa")


if __name__ == "__main__":
    unittest.main()
