import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import count_vowel_substrings
import unittest


class TestCountVowelSubstrings(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertEqual(count_vowel_substrings("aeiouu"), 2)

    def test_example2(self):
        self.assertEqual(count_vowel_substrings("unicornarihan"), 0)

    def test_example3(self):
        self.assertEqual(count_vowel_substrings("cuaieuouac"), 7)

    # Edge cases
    def test_empty_string(self):
        self.assertEqual(count_vowel_substrings(""), 0)

    def test_single_char(self):
        self.assertEqual(count_vowel_substrings("a"), 0)

    def test_all_consonants(self):
        self.assertEqual(count_vowel_substrings("bcdfg"), 0)

    def test_exact_aeiou(self):
        self.assertEqual(count_vowel_substrings("aeiou"), 1)

    def test_consonant_splits_vowels(self):
        self.assertEqual(count_vowel_substrings("aeiobcaeiou"), 1)

    def test_four_vowels_only(self):
        self.assertEqual(count_vowel_substrings("aeio"), 0)


if __name__ == "__main__":
    unittest.main()
