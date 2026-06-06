"""Tests for Check If N and Its Double Exist."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import checkIfExist


class TestCheckIfExist(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertTrue(checkIfExist([10, 2, 5, 3]))

    def test_example2(self):
        self.assertFalse(checkIfExist([3, 1, 7, 11]))

    # Zero edge cases
    def test_two_zeros(self):
        self.assertTrue(checkIfExist([0, 0]))

    def test_single_zero_no_match(self):
        self.assertFalse(checkIfExist([0, 1, 3]))

    # Negative numbers
    def test_negative_double(self):
        self.assertTrue(checkIfExist([-2, -4]))

    def test_negative_no_match(self):
        self.assertFalse(checkIfExist([-3, -7]))

    # Minimum length array
    def test_min_length_true(self):
        self.assertTrue(checkIfExist([2, 4]))

    def test_min_length_false(self):
        self.assertFalse(checkIfExist([1, 3]))

    # Double appears before the number
    def test_double_before_half(self):
        self.assertTrue(checkIfExist([4, 2]))

    # Large values at constraint boundary
    def test_boundary_values(self):
        self.assertFalse(checkIfExist([-103, 103]))


if __name__ == "__main__":
    unittest.main()
