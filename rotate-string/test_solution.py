"""Tests for rotate-string solution."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import can_transform


class TestCanTransform(unittest.TestCase):

    # Problem examples
    def test_example1_rotation(self):
        self.assertTrue(can_transform("abcde", "cdeab"))

    def test_example2_not_rotation(self):
        self.assertFalse(can_transform("abcde", "abced"))

    # Edge cases
    def test_identical_strings(self):
        self.assertTrue(can_transform("abcde", "abcde"))

    def test_single_char(self):
        self.assertTrue(can_transform("a", "a"))

    def test_different_lengths(self):
        self.assertFalse(can_transform("abc", "ab"))

    def test_all_same_chars(self):
        self.assertTrue(can_transform("aaa", "aaa"))

    def test_one_shift(self):
        self.assertTrue(can_transform("abcde", "bcdea"))

    def test_single_char_different(self):
        self.assertFalse(can_transform("a", "b"))

    def test_longer_goal(self):
        self.assertFalse(can_transform("ab", "abc"))


if __name__ == "__main__":
    unittest.main()
