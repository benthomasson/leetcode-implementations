"""Tests for calculate-amount-paid-in-taxes solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import tax_amount


class TestTaxAmount(unittest.TestCase):

    # LeetCode examples
    def test_example1(self):
        self.assertAlmostEqual(tax_amount([[3, 50], [7, 10], [12, 25]], 10), 2.65)

    def test_example2(self):
        self.assertAlmostEqual(tax_amount([[1, 0], [4, 25], [5, 50]], 2), 0.25)

    def test_example3(self):
        self.assertAlmostEqual(tax_amount([[2, 50]], 0), 0.0)

    # Edge cases
    def test_income_at_bracket_boundary(self):
        self.assertAlmostEqual(tax_amount([[3, 50], [7, 10], [12, 25]], 7), 1.9)

    def test_single_bracket_full(self):
        self.assertAlmostEqual(tax_amount([[10, 100]], 10), 10.0)

    def test_zero_percent(self):
        self.assertAlmostEqual(tax_amount([[1000, 0]], 500), 0.0)

    def test_income_equals_max_upper(self):
        self.assertAlmostEqual(tax_amount([[3, 50], [7, 10], [12, 25]], 12), 3.15)

    def test_single_bracket_partial(self):
        self.assertAlmostEqual(tax_amount([[10, 50]], 5), 2.5)

    def test_many_brackets_low_income(self):
        brackets = [[2, 10], [4, 20], [6, 30], [8, 40], [10, 50]]
        self.assertAlmostEqual(tax_amount(brackets, 1), 0.1)


if __name__ == "__main__":
    unittest.main()
