"""Tests for LeetCode 2129: Capitalize the Title."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestCapitalizeTitle(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.capitalizeTitle("capiTalIze tHe titLe"), "Capitalize The Title")

    def test_example2(self):
        self.assertEqual(self.s.capitalizeTitle("First leTTeR of EACH Word"), "First Letter of Each Word")

    def test_example3(self):
        self.assertEqual(self.s.capitalizeTitle("i lOve leetcode"), "i Love Leetcode")

    # --- Edge cases ---
    def test_single_char(self):
        self.assertEqual(self.s.capitalizeTitle("Z"), "z")

    def test_two_char_word(self):
        self.assertEqual(self.s.capitalizeTitle("AB"), "ab")

    def test_three_char_boundary(self):
        self.assertEqual(self.s.capitalizeTitle("ABC"), "Abc")

    def test_all_short_words(self):
        self.assertEqual(self.s.capitalizeTitle("a bb CC"), "a bb cc")

    def test_all_uppercase_input(self):
        self.assertEqual(self.s.capitalizeTitle("HELLO WORLD"), "Hello World")

    def test_all_lowercase_input(self):
        self.assertEqual(self.s.capitalizeTitle("hello world"), "Hello World")

    def test_mixed_short_and_long(self):
        self.assertEqual(self.s.capitalizeTitle("is it A good DAY"), "is it a Good Day")


if __name__ == "__main__":
    unittest.main()
