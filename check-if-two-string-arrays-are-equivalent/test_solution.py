"""Tests for Check If Two String Arrays Are Equivalent."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestArrayStringsAreEqual(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertTrue(self.s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))

    def test_example2(self):
        self.assertFalse(self.s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))

    def test_example3(self):
        self.assertTrue(self.s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))

    # --- Edge cases ---
    def test_single_element_equal(self):
        self.assertTrue(self.s.arrayStringsAreEqual(["abc"], ["abc"]))

    def test_single_char_each(self):
        self.assertTrue(self.s.arrayStringsAreEqual(["a"], ["a"]))

    def test_empty_strings_in_array(self):
        self.assertTrue(self.s.arrayStringsAreEqual(["", "abc", ""], ["abc"]))

    def test_different_content_same_length(self):
        self.assertFalse(self.s.arrayStringsAreEqual(["ab", "cd"], ["ac", "bd"]))

    def test_many_single_chars_vs_one_string(self):
        self.assertTrue(self.s.arrayStringsAreEqual(
            ["a", "b", "c", "d", "e"], ["abcde"]
        ))

    def test_different_concat_lengths(self):
        self.assertFalse(self.s.arrayStringsAreEqual(["a"], ["ab"]))


if __name__ == "__main__":
    unittest.main()
