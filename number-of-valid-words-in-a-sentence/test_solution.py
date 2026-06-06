"""Tests for LeetCode 2047: Number of Valid Words in a Sentence."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestCountValidWords(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(self.s.countValidWords("cat and  dog"), 3)

    def test_example2(self):
        self.assertEqual(self.s.countValidWords("!this  1-s b8d!"), 0)

    def test_example3(self):
        self.assertEqual(self.s.countValidWords("alice and  bob are playing stone-game10"), 5)

    # --- Edge cases ---
    def test_single_punctuation_only(self):
        self.assertEqual(self.s.countValidWords("!"), 1)

    def test_single_letter(self):
        self.assertEqual(self.s.countValidWords("a"), 1)

    def test_only_spaces(self):
        self.assertEqual(self.s.countValidWords("   "), 0)

    def test_hyphen_with_trailing_punct(self):
        self.assertEqual(self.s.countValidWords("a-b."), 1)

    def test_invalid_leading_hyphen(self):
        self.assertEqual(self.s.countValidWords("-ab"), 0)

    def test_invalid_trailing_hyphen(self):
        self.assertEqual(self.s.countValidWords("ab-"), 0)

    def test_invalid_multiple_hyphens(self):
        self.assertEqual(self.s.countValidWords("a-b-c"), 0)

    def test_mixed_valid_and_invalid(self):
        self.assertEqual(self.s.countValidWords("hello world 123 a-b! x-"), 3)


if __name__ == "__main__":
    unittest.main()
