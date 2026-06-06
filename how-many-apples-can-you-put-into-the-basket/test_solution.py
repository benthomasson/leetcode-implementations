"""Tests for How Many Apples Can You Put into the Basket."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import maxNumberOfApples


class TestMaxNumberOfApples(unittest.TestCase):
    def test_example1_all_fit(self):
        self.assertEqual(maxNumberOfApples([100, 200, 150, 1000]), 4)

    def test_example2_one_excluded(self):
        self.assertEqual(maxNumberOfApples([900, 950, 800, 1000, 700, 800]), 5)

    def test_single_apple_fits(self):
        self.assertEqual(maxNumberOfApples([5000]), 1)

    def test_single_apple_too_heavy(self):
        self.assertEqual(maxNumberOfApples([5001]), 0)

    def test_exact_capacity(self):
        self.assertEqual(maxNumberOfApples([1000, 1000, 1000, 1000, 1000]), 5)

    def test_none_fit(self):
        self.assertEqual(maxNumberOfApples([5001, 5002, 5003]), 0)

    def test_all_weight_one(self):
        self.assertEqual(maxNumberOfApples([1] * 1000), 1000)

    def test_minimum_input(self):
        self.assertEqual(maxNumberOfApples([1]), 1)

    def test_max_constraint_weights(self):
        # weight[i] up to 1000, 5 fit exactly at 5000
        self.assertEqual(maxNumberOfApples([1000] * 6), 5)


if __name__ == "__main__":
    unittest.main()
