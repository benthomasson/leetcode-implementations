"""Tests for maximum repeating substring."""

import unittest
from solution import longestAwesomeSubstring


class TestLongestAwesomeSubstring(unittest.TestCase):

    # LeetCode examples
    def test_example1_ab_in_ababc(self):
        self.assertEqual(longestAwesomeSubstring("ababc", "ab"), 2)

    def test_example2_ba_in_ababc(self):
        self.assertEqual(longestAwesomeSubstring("ababc", "ba"), 1)

    def test_example3_ac_not_in_ababc(self):
        self.assertEqual(longestAwesomeSubstring("ababc", "ac"), 0)

    # Edge cases
    def test_word_not_in_sequence(self):
        self.assertEqual(longestAwesomeSubstring("abc", "xyz"), 0)

    def test_word_longer_than_sequence(self):
        self.assertEqual(longestAwesomeSubstring("ab", "abc"), 0)

    def test_word_equals_sequence(self):
        self.assertEqual(longestAwesomeSubstring("abc", "abc"), 1)

    def test_full_repetition_single_char(self):
        self.assertEqual(longestAwesomeSubstring("aaaa", "a"), 4)

    def test_full_repetition_multichar(self):
        self.assertEqual(longestAwesomeSubstring("ababab", "ab"), 3)

    def test_single_char_each(self):
        self.assertEqual(longestAwesomeSubstring("a", "a"), 1)

    def test_repetition_in_middle(self):
        self.assertEqual(longestAwesomeSubstring("xababx", "ab"), 2)


if __name__ == "__main__":
    unittest.main()
