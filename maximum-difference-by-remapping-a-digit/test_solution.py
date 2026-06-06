"""Tests for diffMaxMin - Maximum Difference by Remapping a Digit."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import diffMaxMin


class TestDiffMaxMin(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(diffMaxMin(11891), 99009)

    def test_example2(self):
        self.assertEqual(diffMaxMin(90), 99)

    # Edge cases
    def test_single_digit(self):
        self.assertEqual(diffMaxMin(5), 9)  # max=9, min=0

    def test_single_digit_nine(self):
        self.assertEqual(diffMaxMin(9), 9)  # max=9, min=0

    def test_min_constraint(self):
        self.assertEqual(diffMaxMin(1), 9)  # max=9, min=0

    def test_all_nines(self):
        self.assertEqual(diffMaxMin(9999), 9999)  # max=9999, min=0

    def test_starts_with_nine(self):
        # max: 2->9 = 9988, min: 9->0 = 288, diff=9700
        self.assertEqual(diffMaxMin(9288), 9700)

    def test_all_same_digits(self):
        self.assertEqual(diffMaxMin(1111), 9999)  # max=9999, min=0

    def test_max_constraint(self):
        # 100000000: max 1->9=900000000, min 1->0=0
        self.assertEqual(diffMaxMin(100000000), 900000000)

    def test_already_max_first_digit(self):
        # 91: max: 1->9=99, min: 9->0=01=1, diff=98
        self.assertEqual(diffMaxMin(91), 98)


if __name__ == "__main__":
    unittest.main()
