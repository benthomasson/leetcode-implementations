"""Tests for LeetCode 541: Reverse String II."""

import unittest
from solution import Solution


class TestReverseStr(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.reverseStr("abcdefg", 2), "bacdfeg")

    def test_example2(self):
        self.assertEqual(self.sol.reverseStr("abcd", 2), "bacd")

    def test_k_equals_1(self):
        self.assertEqual(self.sol.reverseStr("abcdef", 1), "abcdef")

    def test_k_greater_than_length(self):
        self.assertEqual(self.sol.reverseStr("abc", 5), "cba")

    def test_single_char(self):
        self.assertEqual(self.sol.reverseStr("a", 1), "a")

    def test_exact_2k(self):
        self.assertEqual(self.sol.reverseStr("abcd", 2), "bacd")

    def test_k_equals_length(self):
        self.assertEqual(self.sol.reverseStr("abcd", 4), "dcba")

    def test_remaining_less_than_k(self):
        # len=5, k=3: reverse first 3 -> "cba" + remaining "de" (less than k, but in second half of window)
        self.assertEqual(self.sol.reverseStr("abcde", 3), "cbade")

    def test_long_string(self):
        self.assertEqual(self.sol.reverseStr("abcdefghij", 3), "cbadefihgj")


if __name__ == "__main__":
    unittest.main()
