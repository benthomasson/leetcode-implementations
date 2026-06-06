"""Tests for Maximum Product of Two Elements in an Array."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import max_product


class TestMaxProduct(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(max_product([3, 4, 5, 2]), 12)

    def test_example2(self):
        self.assertEqual(max_product([1, 5, 4, 5]), 16)

    def test_example3(self):
        self.assertEqual(max_product([3, 7]), 12)

    # Edge cases
    def test_min_length(self):
        self.assertEqual(max_product([1, 1]), 0)

    def test_all_ones(self):
        self.assertEqual(max_product([1, 1, 1, 1]), 0)

    def test_identical_values(self):
        self.assertEqual(max_product([5, 5, 5]), 16)

    def test_max_boundary(self):
        self.assertEqual(max_product([1000, 1000]), 998001)

    def test_descending_order(self):
        self.assertEqual(max_product([5, 4, 3, 2, 1]), 12)

    def test_largest_at_end(self):
        self.assertEqual(max_product([1, 2, 3, 10]), 18)

    def test_large_array(self):
        nums = list(range(1, 501))
        self.assertEqual(max_product(nums), 499 * 498)


if __name__ == "__main__":
    unittest.main()
