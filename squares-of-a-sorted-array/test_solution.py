"""Tests for Squares of a Sorted Array."""

import unittest
from solution import distinctSubseqII


class TestSquaresOfSortedArray(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(distinctSubseqII([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test_example_2(self):
        self.assertEqual(distinctSubseqII([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    def test_all_negative(self):
        self.assertEqual(distinctSubseqII([-5, -3, -1]), [1, 9, 25])

    def test_all_positive(self):
        self.assertEqual(distinctSubseqII([1, 2, 3]), [1, 4, 9])

    def test_single_element(self):
        self.assertEqual(distinctSubseqII([0]), [0])
        self.assertEqual(distinctSubseqII([-5]), [25])

    def test_all_zeros(self):
        self.assertEqual(distinctSubseqII([0, 0, 0]), [0, 0, 0])

    def test_duplicates(self):
        self.assertEqual(distinctSubseqII([-3, -3, 3, 3]), [9, 9, 9, 9])

    def test_large_values(self):
        self.assertEqual(distinctSubseqII([-10000, 10000]), [100000000, 100000000])


if __name__ == "__main__":
    unittest.main()
