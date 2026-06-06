"""Tests for sort even and odd indices independently."""

import sys
import unittest

sys.path.insert(0, "../implementer")

from solution import maxValue


class TestMaxValue(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maxValue([4, 1, 2, 3]), [2, 3, 4, 1])

    def test_example2(self):
        self.assertEqual(maxValue([2, 1]), [2, 1])

    def test_single_element(self):
        self.assertEqual(maxValue([5]), [5])

    def test_all_same(self):
        self.assertEqual(maxValue([3, 3, 3, 3]), [3, 3, 3, 3])

    def test_odd_length(self):
        self.assertEqual(maxValue([5, 3, 1, 2, 4]), [1, 3, 4, 2, 5])

    def test_descending_input(self):
        self.assertEqual(maxValue([6, 5, 4, 3, 2, 1]), [2, 5, 4, 3, 6, 1])

    def test_boundary_values(self):
        self.assertEqual(maxValue([100, 1, 1, 100]), [1, 100, 100, 1])

    def test_max_constraint_values(self):
        self.assertEqual(maxValue([100, 100]), [100, 100])


if __name__ == "__main__":
    unittest.main()
