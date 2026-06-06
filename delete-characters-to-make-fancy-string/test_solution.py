"""Tests for Delete Characters to Make Fancy String."""

import unittest
from solution import Solution


class TestMakeFancyString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.makeFancyString("leeetcode"), "leetcode")

    def test_example2(self):
        self.assertEqual(self.sol.makeFancyString("aaabaaaa"), "aabaa")

    def test_example3(self):
        self.assertEqual(self.sol.makeFancyString("aab"), "aab")

    def test_single_char(self):
        self.assertEqual(self.sol.makeFancyString("a"), "a")

    def test_two_same(self):
        self.assertEqual(self.sol.makeFancyString("aa"), "aa")

    def test_all_same(self):
        self.assertEqual(self.sol.makeFancyString("aaaa"), "aa")

    def test_already_fancy(self):
        self.assertEqual(self.sol.makeFancyString("abcabc"), "abcabc")

    def test_alternating(self):
        self.assertEqual(self.sol.makeFancyString("ababab"), "ababab")

    def test_long_run(self):
        self.assertEqual(self.sol.makeFancyString("aaaaaa"), "aa")


if __name__ == "__main__":
    unittest.main()
