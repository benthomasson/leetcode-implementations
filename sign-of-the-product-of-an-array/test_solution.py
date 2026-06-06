"""Tests for Sign of the Product of an Array."""

import unittest
from solution import signFunc


class TestSignFunc(unittest.TestCase):
    # Provided examples
    def test_example1(self):
        self.assertEqual(signFunc([-1, -2, -3, -4, 3, 2, 1]), 1)

    def test_example2(self):
        self.assertEqual(signFunc([1, 5, 0, 2, -3]), 0)

    def test_example3(self):
        self.assertEqual(signFunc([-1, 1, -1, 1, -1]), -1)

    # Edge cases
    def test_single_positive(self):
        self.assertEqual(signFunc([1]), 1)

    def test_single_negative(self):
        self.assertEqual(signFunc([-1]), -1)

    def test_single_zero(self):
        self.assertEqual(signFunc([0]), 0)

    def test_all_positive(self):
        self.assertEqual(signFunc([1, 2, 3]), 1)

    def test_even_negatives(self):
        self.assertEqual(signFunc([-1, -2]), 1)

    def test_odd_negatives(self):
        self.assertEqual(signFunc([-1, -2, -3]), -1)

    def test_boundary_values(self):
        self.assertEqual(signFunc([-100, 100]), -1)

    def test_zero_among_negatives(self):
        self.assertEqual(signFunc([-1, 0, -1]), 0)


if __name__ == "__main__":
    unittest.main()
