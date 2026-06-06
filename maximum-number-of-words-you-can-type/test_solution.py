"""Tests for Maximum Number of Words You Can Type."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.min_operations("hello world", "ad"), 1)

    def test_example2(self):
        self.assertEqual(self.s.min_operations("leet code", "lt"), 1)

    def test_example3(self):
        self.assertEqual(self.s.min_operations("leet code", "e"), 0)

    # --- Edge cases ---
    def test_no_broken_letters(self):
        self.assertEqual(self.s.min_operations("hello world", ""), 2)

    def test_single_word_typeable(self):
        self.assertEqual(self.s.min_operations("hello", "z"), 1)

    def test_single_word_not_typeable(self):
        self.assertEqual(self.s.min_operations("hello", "h"), 0)

    def test_single_char_words(self):
        self.assertEqual(self.s.min_operations("a b c d", "b"), 3)

    def test_all_words_typeable(self):
        self.assertEqual(self.s.min_operations("abc def ghi", "z"), 3)

    def test_no_words_typeable(self):
        self.assertEqual(self.s.min_operations("abc def", "abcdef"), 0)

    def test_all_26_broken(self):
        self.assertEqual(self.s.min_operations("test", "abcdefghijklmnopqrstuvwxyz"), 0)


if __name__ == "__main__":
    unittest.main()
