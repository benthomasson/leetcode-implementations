"""Tests for Construct the Rectangle solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import constructRectangle


class TestConstructRectangle(unittest.TestCase):
    # --- Problem examples ---
    def test_example1_perfect_square(self):
        self.assertEqual(constructRectangle(4), [2, 2])

    def test_example2_prime(self):
        self.assertEqual(constructRectangle(37), [37, 1])

    def test_example3_large(self):
        self.assertEqual(constructRectangle(122122), [427, 286])

    # --- Edge cases ---
    def test_min_area(self):
        self.assertEqual(constructRectangle(1), [1, 1])

    def test_max_area(self):
        result = constructRectangle(10**7)
        self.assertEqual(result[0] * result[1], 10**7)
        self.assertGreaterEqual(result[0], result[1])

    def test_composite(self):
        self.assertEqual(constructRectangle(12), [4, 3])

    # --- Invariant checks ---
    def test_area_product_holds(self):
        for area in [1, 2, 6, 15, 100, 9999991]:
            result = constructRectangle(area)
            self.assertEqual(result[0] * result[1], area, f"area={area}")
            self.assertGreaterEqual(result[0], result[1], f"L < W for area={area}")


if __name__ == "__main__":
    unittest.main()
