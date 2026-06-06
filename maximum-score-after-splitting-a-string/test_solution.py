"""Tests for maximum score after splitting a string."""

import unittest
from solution import is_possible_divide


class TestIsPossibleDivide(unittest.TestCase):
    # Provided examples
    def test_example1(self):
        self.assertEqual(is_possible_divide("011101"), 5)

    def test_example2(self):
        self.assertEqual(is_possible_divide("00111"), 5)

    def test_example3(self):
        self.assertEqual(is_possible_divide("1111"), 3)

    # Length-2 edge cases
    def test_01(self):
        self.assertEqual(is_possible_divide("01"), 2)

    def test_10(self):
        self.assertEqual(is_possible_divide("10"), 0)

    def test_00(self):
        self.assertEqual(is_possible_divide("00"), 1)

    def test_11(self):
        self.assertEqual(is_possible_divide("11"), 1)

    # Uniform strings
    def test_all_zeros(self):
        self.assertEqual(is_possible_divide("00000"), 4)

    def test_all_ones(self):
        self.assertEqual(is_possible_divide("11111"), 4)

    # Best split at last position
    def test_best_split_late(self):
        self.assertEqual(is_possible_divide("00001"), 5)


if __name__ == "__main__":
    unittest.main()
