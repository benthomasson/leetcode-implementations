"""Tests for Number of Different Integers in a String."""
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import num_different_integers


class TestNumDifferentIntegers(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(num_different_integers("a123bc34d8ef34"), 3)

    def test_example2(self):
        self.assertEqual(num_different_integers("leet1234code234"), 2)

    def test_example3_leading_zeros(self):
        self.assertEqual(num_different_integers("a1b01c001"), 1)

    # Edge cases
    def test_all_letters(self):
        self.assertEqual(num_different_integers("abc"), 0)

    def test_all_digits(self):
        self.assertEqual(num_different_integers("12345"), 1)

    def test_single_zero(self):
        self.assertEqual(num_different_integers("0"), 1)

    def test_multiple_zeros_separated(self):
        self.assertEqual(num_different_integers("0a0b0"), 1)

    def test_single_char(self):
        self.assertEqual(num_different_integers("a"), 0)

    def test_large_leading_zeros(self):
        self.assertEqual(num_different_integers("a000123b000123c"), 1)

    def test_distinct_numbers(self):
        self.assertEqual(num_different_integers("a1b2c3d4e5"), 5)


if __name__ == "__main__":
    unittest.main()
