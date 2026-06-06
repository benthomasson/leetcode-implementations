"""Tests for to_hex solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import to_hex


class TestToHex(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(to_hex(26), "1a")

    def test_example2(self):
        self.assertEqual(to_hex(-1), "ffffffff")

    # Edge cases
    def test_zero(self):
        self.assertEqual(to_hex(0), "0")

    def test_one(self):
        self.assertEqual(to_hex(1), "1")

    def test_boundary_single_hex_digit(self):
        self.assertEqual(to_hex(15), "f")

    def test_boundary_two_hex_digits(self):
        self.assertEqual(to_hex(16), "10")

    def test_int_max(self):
        self.assertEqual(to_hex(2**31 - 1), "7fffffff")

    def test_int_min(self):
        self.assertEqual(to_hex(-(2**31)), "80000000")

    def test_small_negative(self):
        self.assertEqual(to_hex(-2), "fffffffe")

    def test_positive_255(self):
        self.assertEqual(to_hex(255), "ff")


if __name__ == "__main__":
    unittest.main()
