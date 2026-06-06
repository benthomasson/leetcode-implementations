"""Tests for check-if-one-string-swap-can-make-strings-equal."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import are_almost_equal


class TestAreAlmostEqual(unittest.TestCase):
    # LeetCode examples
    def test_example1_swap_needed(self):
        self.assertTrue(are_almost_equal("bank", "kanb"))

    def test_example2_impossible(self):
        self.assertFalse(are_almost_equal("attack", "defend"))

    def test_example3_already_equal(self):
        self.assertTrue(are_almost_equal("kelb", "kelb"))

    # Edge cases
    def test_single_char_equal(self):
        self.assertTrue(are_almost_equal("a", "a"))

    def test_single_char_different(self):
        self.assertFalse(are_almost_equal("a", "b"))

    def test_one_mismatch_cannot_swap(self):
        self.assertFalse(are_almost_equal("ab", "ac"))

    def test_two_diffs_wrong_chars(self):
        self.assertFalse(are_almost_equal("ab", "cd"))

    def test_three_diffs(self):
        self.assertFalse(are_almost_equal("abcd", "dcba"))

    def test_adjacent_swap(self):
        self.assertTrue(are_almost_equal("ab", "ba"))

    def test_all_same_chars(self):
        self.assertTrue(are_almost_equal("aaaa", "aaaa"))


if __name__ == "__main__":
    unittest.main()
