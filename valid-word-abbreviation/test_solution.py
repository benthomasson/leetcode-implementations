"""Tests for Valid Word Abbreviation."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import validWordAbbreviation


class TestValidWordAbbreviation(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertTrue(validWordAbbreviation("internationalization", "i12iz4n"))

    def test_example2(self):
        self.assertFalse(validWordAbbreviation("apple", "a2e"))

    # Edge cases
    def test_full_word_as_number(self):
        self.assertTrue(validWordAbbreviation("substitution", "12"))

    def test_no_abbreviation(self):
        self.assertTrue(validWordAbbreviation("word", "word"))

    def test_leading_zero(self):
        self.assertFalse(validWordAbbreviation("substitution", "s010n"))

    def test_zero_length_replacement(self):
        self.assertFalse(validWordAbbreviation("ab", "a0b"))

    def test_number_exceeds_word(self):
        self.assertFalse(validWordAbbreviation("hi", "9"))

    def test_single_char_as_number(self):
        self.assertTrue(validWordAbbreviation("a", "1"))

    def test_char_mismatch(self):
        self.assertFalse(validWordAbbreviation("a", "b"))

    def test_abbr_too_short(self):
        self.assertFalse(validWordAbbreviation("apple", "a2"))


if __name__ == "__main__":
    unittest.main()
