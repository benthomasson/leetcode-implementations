"""Tests for min_operations."""

import unittest
from solution import min_operations


class TestMinOperations(unittest.TestCase):
    def test_all_ones(self):
        self.assertEqual(min_operations([1, 1, 1]), 3)

    def test_mixed(self):
        self.assertEqual(min_operations([1, 5, 2, 4, 1]), 14)

    def test_single(self):
        self.assertEqual(min_operations([8]), 0)

    def test_already_increasing(self):
        self.assertEqual(min_operations([1, 2, 3, 4]), 0)

    def test_descending(self):
        self.assertEqual(min_operations([5, 4, 3, 2, 1]), 20)

    def test_all_equal(self):
        self.assertEqual(min_operations([3, 3, 3, 3]), 6)

    def test_two_elements_equal(self):
        self.assertEqual(min_operations([1, 1]), 1)

    def test_two_elements_increasing(self):
        self.assertEqual(min_operations([1, 2]), 0)


if __name__ == "__main__":
    unittest.main()
