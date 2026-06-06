"""Tests for Goat Latin solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import number_of_lines


class TestGoatLatin(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertEqual(
            number_of_lines("I speak Goat Latin"),
            "Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
        )

    def test_example2(self):
        self.assertEqual(
            number_of_lines("The quick brown fox jumped over the lazy dog"),
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
        )

    # Edge cases
    def test_single_vowel_word(self):
        self.assertEqual(number_of_lines("apple"), "applemaa")

    def test_single_consonant_word(self):
        self.assertEqual(number_of_lines("goat"), "oatgmaa")

    def test_single_letter_vowel(self):
        self.assertEqual(number_of_lines("I"), "Imaa")

    def test_single_letter_consonant(self):
        self.assertEqual(number_of_lines("b"), "bmaa")

    def test_uppercase_vowel(self):
        self.assertEqual(number_of_lines("Each"), "Eachmaa")

    def test_all_vowels(self):
        self.assertEqual(
            number_of_lines("a e i o u"),
            "amaa emaaa imaaaa omaaaaa umaaaaaa",
        )

    def test_mixed_case_consonants(self):
        self.assertEqual(number_of_lines("Hello World"), "elloHmaa orldWmaaa")

    def test_two_letter_words(self):
        self.assertEqual(number_of_lines("go is"), "ogmaa ismaaa")


if __name__ == "__main__":
    unittest.main()
