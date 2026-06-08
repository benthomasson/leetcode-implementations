"""Tests for Replace All Digits With Characters - LeetCode 1844."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution, replace_digits


class TestReplaceDigits(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().replaceDigits

    # Problem examples
    def test_example1(self):
        self.assertEqual(self.solve("a1c1e1"), "abcdef")

    def test_example2(self):
        self.assertEqual(self.solve("a1b2c3d4e"), "abbdcfdhe")

    # Edge cases
    def test_single_char(self):
        self.assertEqual(self.solve("a"), "a")

    def test_zero_shift(self):
        self.assertEqual(self.solve("a0"), "aa")

    def test_near_z(self):
        self.assertEqual(self.solve("z0"), "zz")

    def test_max_shift(self):
        self.assertEqual(self.solve("a9"), "aj")

    def test_all_same_letter(self):
        self.assertEqual(self.solve("a0a0a0"), "aaaaaa")

    def test_replace_digits_alias(self):
        self.assertEqual(replace_digits("a1c1e1"), "abcdef")


if __name__ == "__main__":
    unittest.main()
