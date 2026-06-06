"""Tests for Minimum Changes to Make Alternating Binary String."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import canDistribute


class TestCanDistribute(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(canDistribute("0100"), 1)

    def test_example2(self):
        self.assertEqual(canDistribute("10"), 0)

    def test_example3(self):
        self.assertEqual(canDistribute("1111"), 2)

    # Edge cases
    def test_single_0(self):
        self.assertEqual(canDistribute("0"), 0)

    def test_single_1(self):
        self.assertEqual(canDistribute("1"), 0)

    def test_already_alternating_01(self):
        self.assertEqual(canDistribute("0101"), 0)

    def test_already_alternating_10(self):
        self.assertEqual(canDistribute("1010"), 0)

    def test_all_zeros_even(self):
        self.assertEqual(canDistribute("0000"), 2)

    def test_all_ones_odd(self):
        self.assertEqual(canDistribute("111"), 1)

    def test_half_flipped(self):
        # "0011" vs "0101": mismatches at pos 1,2 -> count=2, min(2,2)=2
        self.assertEqual(canDistribute("0011"), 2)

    def test_long_string(self):
        s = "01" * 5000  # length 10000, already alternating
        self.assertEqual(canDistribute(s), 0)


if __name__ == "__main__":
    unittest.main()
