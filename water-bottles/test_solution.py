"""Tests for Water Bottles solution."""

import unittest
from solution import numWaterBottles


class TestNumWaterBottles(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(numWaterBottles(9, 3), 13)

    def test_example2(self):
        self.assertEqual(numWaterBottles(15, 4), 19)

    def test_no_exchange_possible(self):
        self.assertEqual(numWaterBottles(1, 2), 1)

    def test_exact_exchange(self):
        self.assertEqual(numWaterBottles(2, 2), 3)

    def test_large_values(self):
        self.assertEqual(numWaterBottles(100, 2), 199)

    def test_high_exchange_rate(self):
        self.assertEqual(numWaterBottles(5, 100), 5)


if __name__ == "__main__":
    unittest.main()
