"""Tests for LeetCode 1078: Occurrences After Bigram."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestFindOcurrences(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.findOcurrences("alice is a good girl she is a good student", "a", "good"),
            ["girl", "student"],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.findOcurrences("we will we will rock you", "we", "will"),
            ["we", "rock"],
        )

    def test_no_match(self):
        self.assertEqual(self.s.findOcurrences("hello world foo", "a", "b"), [])

    def test_bigram_at_end_no_third(self):
        self.assertEqual(self.s.findOcurrences("a b", "a", "b"), [])

    def test_overlapping_pattern(self):
        self.assertEqual(self.s.findOcurrences("a a a a", "a", "a"), ["a", "a"])

    def test_single_word(self):
        self.assertEqual(self.s.findOcurrences("hello", "hello", "world"), [])

    def test_first_equals_second(self):
        self.assertEqual(self.s.findOcurrences("x x y x x z", "x", "x"), ["y", "z"])

    def test_three_words_exact_match(self):
        self.assertEqual(self.s.findOcurrences("a b c", "a", "b"), ["c"])

    def test_multiple_consecutive_matches(self):
        self.assertEqual(
            self.s.findOcurrences("a b x a b y a b z", "a", "b"),
            ["x", "y", "z"],
        )


if __name__ == "__main__":
    unittest.main()
