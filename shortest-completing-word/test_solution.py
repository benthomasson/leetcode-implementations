"""Tests for Shortest Completing Word solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import shortestCompletingWord


class TestShortestCompletingWord(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]),
            "steps",
        )

    def test_example2(self):
        self.assertEqual(
            shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]),
            "pest",
        )

    def test_single_letter_plate(self):
        self.assertEqual(shortestCompletingWord("a", ["b", "a", "aa"]), "a")

    def test_tie_break_first_occurrence(self):
        self.assertEqual(shortestCompletingWord("a", ["ab", "ac", "ad"]), "ab")

    def test_mixed_case_plate(self):
        self.assertEqual(
            shortestCompletingWord("aBc 12c", ["abcc", "cbca", "abccdef"]), "abcc"
        )

    def test_repeated_letters(self):
        self.assertEqual(shortestCompletingWord("AA", ["a", "aa", "aaa"]), "aa")

    def test_plate_all_digits_one_letter(self):
        self.assertEqual(shortestCompletingWord("1 2 3 z", ["az", "z", "zz"]), "z")

    def test_single_word(self):
        self.assertEqual(shortestCompletingWord("a", ["a"]), "a")

    def test_word_with_extra_letters(self):
        self.assertEqual(shortestCompletingWord("b", ["abc", "b"]), "b")


if __name__ == "__main__":
    unittest.main()
