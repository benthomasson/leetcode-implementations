"""Tests for canFormArray."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import canFormArray


class TestCanFormArray(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertTrue(canFormArray([15, 88], [[88], [15]]))

    def test_example2(self):
        self.assertFalse(canFormArray([49, 18, 16], [[16, 18, 49]]))

    def test_example3(self):
        self.assertTrue(canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))

    # Edge cases
    def test_single_element(self):
        self.assertTrue(canFormArray([1], [[1]]))

    def test_single_piece_full_match(self):
        self.assertTrue(canFormArray([1, 2, 3], [[1, 2, 3]]))

    def test_single_piece_wrong_order(self):
        self.assertFalse(canFormArray([1, 2, 3], [[3, 2, 1]]))

    def test_all_singletons(self):
        self.assertTrue(canFormArray([3, 1, 2], [[1], [2], [3]]))

    def test_piece_partial_mismatch(self):
        """Piece starts at right position but has wrong subsequent elements."""
        self.assertFalse(canFormArray([1, 2, 3], [[1, 3], [2]]))

    def test_two_multi_element_pieces(self):
        self.assertTrue(canFormArray([5, 6, 3, 4], [[3, 4], [5, 6]]))


if __name__ == "__main__":
    unittest.main()
