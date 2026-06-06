"""Tests for keyboard-row solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import find_words


class TestFindWords(unittest.TestCase):

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(find_words(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

    def test_example2(self):
        self.assertEqual(find_words(["omk"]), [])

    def test_example3(self):
        self.assertEqual(find_words(["adsdf", "sfd"]), ["adsdf", "sfd"])

    # Edge cases
    def test_single_char_each_row(self):
        self.assertEqual(find_words(["q", "a", "z"]), ["q", "a", "z"])

    def test_all_uppercase(self):
        self.assertEqual(find_words(["TYPEWRITER"]), ["TYPEWRITER"])

    def test_mixed_case_preserved(self):
        self.assertEqual(find_words(["AlAsKa"]), ["AlAsKa"])

    def test_no_words_match(self):
        self.assertEqual(find_words(["Hello", "World"]), [])

    def test_row1_only(self):
        self.assertEqual(find_words(["qwerty", "quest"]), ["qwerty"])

    def test_row2_only(self):
        self.assertEqual(find_words(["flash", "sad"]), ["flash", "sad"])

    def test_row3_only(self):
        self.assertEqual(find_words(["bnm", "cvb"]), ["bnm", "cvb"])


if __name__ == "__main__":
    unittest.main()
