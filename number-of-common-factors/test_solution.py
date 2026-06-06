"""Tests for common_factors."""

import unittest
from solution import common_factors


class TestCommonFactors(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(common_factors(12, 6), 4)

    def test_example2(self):
        self.assertEqual(common_factors(25, 30), 2)

    def test_coprime(self):
        self.assertEqual(common_factors(7, 13), 1)

    def test_equal(self):
        self.assertEqual(common_factors(6, 6), 4)

    def test_one_and_one(self):
        self.assertEqual(common_factors(1, 1), 1)

    def test_one_and_large(self):
        self.assertEqual(common_factors(1, 1000), 1)

    def test_one_divides_other(self):
        self.assertEqual(common_factors(4, 16), 3)  # 1, 2, 4

    def test_max_constraints(self):
        self.assertEqual(common_factors(1000, 1000), 16)  # divisors of 1000

    def test_perfect_square_gcd(self):
        self.assertEqual(common_factors(36, 36), 9)  # divisors of 36


if __name__ == "__main__":
    unittest.main()
