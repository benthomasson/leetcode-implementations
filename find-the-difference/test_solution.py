"""Tests for Find the Difference."""

import unittest
from solution import findTheDifference


class TestFindTheDifference(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(findTheDifference("abcd", "abcde"), "e")

    def test_example2(self):
        self.assertEqual(findTheDifference("", "y"), "y")

    def test_single_char_duplicated(self):
        self.assertEqual(findTheDifference("a", "aa"), "a")

    def test_all_same_chars(self):
        self.assertEqual(findTheDifference("aaa", "aaaa"), "a")

    def test_extra_at_beginning(self):
        self.assertEqual(findTheDifference("abc", "zabc"), "z")

    def test_extra_at_middle(self):
        self.assertEqual(findTheDifference("abc", "abxc"), "x")

    def test_extra_at_end(self):
        self.assertEqual(findTheDifference("abc", "abcd"), "d")

    def test_long_string(self):
        s = "abcdefghij" * 100
        t = sorted(s + "z")
        self.assertEqual(findTheDifference(s, "".join(t)), "z")


if __name__ == "__main__":
    unittest.main()
