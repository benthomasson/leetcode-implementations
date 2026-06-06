"""Tests for LeetCode 1945: Sum of Digits of String After Convert."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestGetLucky(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1_iiii_k1(self):
        self.assertEqual(self.sol.getLucky("iiii", 1), 36)

    def test_example2_leetcode_k2(self):
        self.assertEqual(self.sol.getLucky("leetcode", 2), 6)

    def test_example3_zbax_k2(self):
        self.assertEqual(self.sol.getLucky("zbax", 2), 8)

    # --- Edge cases ---
    def test_single_char_a(self):
        # a -> 1 -> 1
        self.assertEqual(self.sol.getLucky("a", 1), 1)

    def test_single_char_z(self):
        # z -> "26" -> 2+6=8
        self.assertEqual(self.sol.getLucky("z", 1), 8)

    def test_k_equals_1_no_extra_transform(self):
        # "ab" -> "12" -> 1+2=3 (only 1 transform)
        self.assertEqual(self.sol.getLucky("ab", 1), 3)

    def test_large_k_stabilizes(self):
        # zzzz -> "26262626" -> 32 -> 5 -> 5 -> ... stabilizes at 5
        self.assertEqual(self.sol.getLucky("zzzz", 10), 5)

    def test_long_string(self):
        # 100 'a's -> "1" * 100 -> sum = 100 -> 1+0+0=1
        self.assertEqual(self.sol.getLucky("a" * 100, 1), 100)
        self.assertEqual(self.sol.getLucky("a" * 100, 2), 1)


if __name__ == "__main__":
    unittest.main()
