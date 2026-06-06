"""Tests for LeetCode 819: Most Common Word."""

import unittest

from solution import Solution


class TestMostCommonWord(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), "ball")

    def test_example2(self):
        paragraph = "a."
        banned = []
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), "a")

    def test_no_banned_words(self):
        paragraph = "hello hello world"
        self.assertEqual(self.s.mostCommonWord(paragraph, []), "hello")

    def test_single_word(self):
        self.assertEqual(self.s.mostCommonWord("word", []), "word")

    def test_case_insensitive(self):
        paragraph = "Apple APPLE aPpLe banana"
        self.assertEqual(self.s.mostCommonWord(paragraph, []), "apple")

    def test_all_punctuation_types(self):
        paragraph = "a! b? c' d, e; f."
        self.assertEqual(self.s.mostCommonWord(paragraph, []), "a")

    def test_punctuation_adjacent_to_words(self):
        paragraph = "yes!yes!yes no"
        self.assertEqual(self.s.mostCommonWord(paragraph, []), "yes")

    def test_banned_word_not_in_paragraph(self):
        paragraph = "cat dog cat"
        banned = ["fish"]
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), "cat")

    def test_most_frequent_is_banned(self):
        paragraph = "a a a b b c"
        banned = ["a"]
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), "b")

    def test_multiple_banned_words(self):
        paragraph = "a a a b b b c c d"
        banned = ["a", "b"]
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), "c")

    def test_consecutive_spaces_and_punctuation(self):
        paragraph = "hello...  world,,, hello"
        self.assertEqual(self.s.mostCommonWord(paragraph, []), "hello")

    def test_all_same_word(self):
        paragraph = "bob bob bob"
        self.assertEqual(self.s.mostCommonWord(paragraph, []), "bob")

    def test_only_one_non_banned(self):
        paragraph = "a b c d e"
        banned = ["a", "b", "c", "d"]
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), "e")


if __name__ == "__main__":
    unittest.main()
