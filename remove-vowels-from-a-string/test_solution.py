import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution

import unittest


class TestRemoveVowels(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.removeVowels("leetcodeisacommunityforcoders"), "ltcdscmmntyfrcdrs")

    def test_example2(self):
        self.assertEqual(self.sol.removeVowels("aeiou"), "")

    def test_no_vowels(self):
        self.assertEqual(self.sol.removeVowels("bcdfg"), "bcdfg")

    def test_single_vowel(self):
        self.assertEqual(self.sol.removeVowels("a"), "")

    def test_single_consonant(self):
        self.assertEqual(self.sol.removeVowels("z"), "z")

    def test_mixed_short(self):
        self.assertEqual(self.sol.removeVowels("abc"), "bc")

    def test_all_same_vowel(self):
        self.assertEqual(self.sol.removeVowels("aaaa"), "")

    def test_long_string(self):
        s = "ab" * 500  # length 1000
        self.assertEqual(self.sol.removeVowels(s), "b" * 500)


if __name__ == "__main__":
    unittest.main()
