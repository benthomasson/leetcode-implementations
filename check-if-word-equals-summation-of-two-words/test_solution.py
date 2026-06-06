"""Tests for Check If Word Equals Summation of Two Words."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestIsSumEqual(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        # "acb"->21, "cba"->210, "cdb"->231; 21+210==231
        self.assertTrue(self.s.isSumEqual("acb", "cba", "cdb"))

    def test_example2(self):
        # "aaa"->0, "a"->0, "aab"->1; 0+0!=1
        self.assertFalse(self.s.isSumEqual("aaa", "a", "aab"))

    def test_example3(self):
        # all zeros
        self.assertTrue(self.s.isSumEqual("aaa", "a", "aaaa"))

    # --- Edge cases ---
    def test_single_char_true(self):
        # b(1)+c(2)==d(3)
        self.assertTrue(self.s.isSumEqual("b", "c", "d"))

    def test_single_char_false(self):
        # a(0)+a(0)!=b(1)
        self.assertFalse(self.s.isSumEqual("a", "a", "b"))

    def test_all_zeros(self):
        self.assertTrue(self.s.isSumEqual("a", "a", "a"))

    def test_max_digit_with_carry(self):
        # "jj"->99, 99+99=198; "bji"->198
        self.assertTrue(self.s.isSumEqual("jj", "jj", "bji"))

    def test_different_lengths(self):
        # "j"->9, "aj"->9; 9+9=18; "bi"->18
        self.assertTrue(self.s.isSumEqual("j", "aj", "bi"))

    def test_max_length_false(self):
        # "jjjjjjjj"->99999999, "a"->0; target "a"->0; 99999999!=0
        self.assertFalse(self.s.isSumEqual("jjjjjjjj", "a", "a"))


if __name__ == "__main__":
    unittest.main()
