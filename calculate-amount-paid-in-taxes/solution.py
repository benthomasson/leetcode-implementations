"""Calculate amount paid in taxes using progressive tax brackets."""

import unittest


def tax_amount(brackets: list[list[int]], income: int) -> float:
    """Calculate total tax owed given progressive tax brackets and income.

    Args:
        brackets: Sorted list of [upper_bound, percent] pairs.
        income: Total income earned.

    Returns:
        Total tax amount owed.
    """
    tax = 0.0
    prev = 0
    for upper, percent in brackets:
        taxable = min(upper, income) - prev
        if taxable <= 0:
            break
        tax += taxable * percent / 100
        prev = upper
    return tax


class TestTaxAmount(unittest.TestCase):

    def test_example1(self):
        self.assertAlmostEqual(tax_amount([[3, 50], [7, 10], [12, 25]], 10), 2.65)

    def test_example2(self):
        self.assertAlmostEqual(tax_amount([[1, 0], [4, 25], [5, 50]], 2), 0.25)

    def test_example3(self):
        self.assertAlmostEqual(tax_amount([[2, 50]], 0), 0.0)

    def test_income_at_bracket_boundary(self):
        self.assertAlmostEqual(tax_amount([[3, 50], [7, 10], [12, 25]], 7), 1.9)

    def test_single_bracket_full(self):
        self.assertAlmostEqual(tax_amount([[10, 100]], 10), 10.0)

    def test_zero_percent(self):
        self.assertAlmostEqual(tax_amount([[1000, 0]], 500), 0.0)

    def test_all_100_percent(self):
        self.assertAlmostEqual(tax_amount([[5, 100], [10, 100]], 8), 8.0)


if __name__ == "__main__":
    unittest.main()
