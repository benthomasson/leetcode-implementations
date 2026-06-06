"""Tests for Long Pressed Name solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestLongPressedName(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # Problem examples
    def test_example1_alex(self):
        self.assertTrue(self.s.isLongPressedName("alex", "aaleex"))

    def test_example2_saeed(self):
        self.assertFalse(self.s.isLongPressedName("saeed", "ssaaedd"))

    # Edge cases
    def test_identical_strings(self):
        self.assertTrue(self.s.isLongPressedName("abc", "abc"))

    def test_single_char_long_press(self):
        self.assertTrue(self.s.isLongPressedName("a", "aaa"))

    def test_typed_shorter_than_name(self):
        self.assertFalse(self.s.isLongPressedName("abc", "ab"))

    def test_wrong_char_in_typed(self):
        self.assertFalse(self.s.isLongPressedName("a", "b"))

    def test_extra_different_char_at_end(self):
        self.assertFalse(self.s.isLongPressedName("alex", "aaleexa"))

    def test_empty_typed(self):
        self.assertFalse(self.s.isLongPressedName("a", ""))

    # LeetCode known tricky case: repeated chars in name
    def test_repeated_chars_in_name(self):
        self.assertTrue(self.s.isLongPressedName("leelee", "lleeelee"))

    def test_name_has_more_repeats_than_typed(self):
        self.assertFalse(self.s.isLongPressedName("aaa", "aa"))


if __name__ == "__main__":
    unittest.main()
