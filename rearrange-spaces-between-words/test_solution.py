"""Tests for reorderSpaces."""

import unittest
from solution import reorderSpaces


class TestReorderSpaces(unittest.TestCase):

    def test_example1(self):
        # 9 spaces, 4 words -> 9//3=3 between, 0 extra
        text = "  this   is  a sentence "
        self.assertEqual(reorderSpaces(text), "this   is   a   sentence")

    def test_example2(self):
        # 7 spaces, 3 words -> 7//2=3 between, 1 extra
        text = " practice   makes   perfect"
        self.assertEqual(reorderSpaces(text), "practice   makes   perfect ")

    def test_single_word_no_spaces(self):
        self.assertEqual(reorderSpaces("hello"), "hello")

    def test_single_word_with_spaces(self):
        self.assertEqual(reorderSpaces("  hello  "), "hello    ")

    def test_two_words(self):
        self.assertEqual(reorderSpaces("a   b"), "a   b")

    def test_preserves_length(self):
        text = "  this   is  a sentence  "
        self.assertEqual(len(reorderSpaces(text)), len(text))

    def test_all_spaces_one_word(self):
        self.assertEqual(reorderSpaces("   a   "), "a      ")


if __name__ == "__main__":
    unittest.main()
