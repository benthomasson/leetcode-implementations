"""Tests for distribute money to maximum children."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import maximum_children_with_eight_dollars


class TestMaximumChildrenWithEightDollars(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(maximum_children_with_eight_dollars(20, 3), 1)

    def test_example2(self):
        self.assertEqual(maximum_children_with_eight_dollars(16, 2), 2)

    # Impossible case
    def test_not_enough_money(self):
        self.assertEqual(maximum_children_with_eight_dollars(1, 2), -1)

    # Everyone gets minimum ($1 each)
    def test_exact_minimum(self):
        self.assertEqual(maximum_children_with_eight_dollars(2, 2), 0)

    # All children get exactly $8
    def test_all_get_eight(self):
        self.assertEqual(maximum_children_with_eight_dollars(24, 3), 3)

    # All could get $8 but surplus forces one to take extra
    def test_surplus_reduces_eights(self):
        self.assertEqual(maximum_children_with_eight_dollars(17, 2), 1)

    # Remaining child would get $4 (forbidden) — must reduce
    def test_avoid_four_dollars(self):
        self.assertEqual(maximum_children_with_eight_dollars(12, 2), 0)

    # Large money, few children — surplus edge case
    def test_large_money(self):
        self.assertEqual(maximum_children_with_eight_dollars(200, 2), 1)

    # Many children, just enough for $1 each
    def test_many_children_min_money(self):
        self.assertEqual(maximum_children_with_eight_dollars(30, 30), 0)

    # Boundary: money equals children (everyone gets $1)
    def test_money_equals_children(self):
        self.assertEqual(maximum_children_with_eight_dollars(8, 8), 0)


if __name__ == "__main__":
    unittest.main()
