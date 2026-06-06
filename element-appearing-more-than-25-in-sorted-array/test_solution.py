"""Tests for Element Appearing More Than 25% in Sorted Array."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import find_special_integer


class TestFindSpecialInteger(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)

    def test_example2(self):
        self.assertEqual(find_special_integer([1, 1]), 1)

    def test_single_element(self):
        self.assertEqual(find_special_integer([5]), 5)

    def test_all_same(self):
        self.assertEqual(find_special_integer([3, 3, 3, 3]), 3)

    def test_dominant_at_start(self):
        self.assertEqual(find_special_integer([1, 1, 1, 2, 3, 4, 5, 6, 7, 8]), 1)

    def test_dominant_at_end(self):
        self.assertEqual(find_special_integer([1, 2, 3, 4, 5, 6, 7, 8, 8, 8]), 8)

    def test_dominant_in_middle(self):
        self.assertEqual(find_special_integer([1, 2, 5, 5, 5, 5, 7, 8]), 5)

    def test_minimum_values(self):
        self.assertEqual(find_special_integer([0, 0, 0, 1]), 0)


if __name__ == "__main__":
    unittest.main()
