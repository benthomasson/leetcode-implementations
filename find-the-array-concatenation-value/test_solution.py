"""Tests for Find the Array Concatenation Value."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import concatenationValue


class TestConcatenationValue(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(concatenationValue([7, 52, 2, 4]), 596)

    def test_example2(self):
        self.assertEqual(concatenationValue([5, 14, 13, 8, 12]), 673)

    def test_single_element(self):
        self.assertEqual(concatenationValue([42]), 42)

    def test_two_elements(self):
        self.assertEqual(concatenationValue([15, 49]), 1549)

    def test_single_digit_pair(self):
        # [1, 2] -> concat(1,2) = 12
        self.assertEqual(concatenationValue([1, 2]), 12)

    def test_odd_length_with_middle(self):
        # [1, 2, 3] -> concat(1,3)=13, middle=2 -> 15
        self.assertEqual(concatenationValue([1, 2, 3]), 15)

    def test_max_values(self):
        # [10000, 10000] -> concat = 1000010000
        self.assertEqual(concatenationValue([10000, 10000]), 1000010000)

    def test_min_value(self):
        self.assertEqual(concatenationValue([1]), 1)

    def test_four_same_digits(self):
        # [5, 5, 5, 5] -> concat(5,5)=55, concat(5,5)=55 -> 110
        self.assertEqual(concatenationValue([5, 5, 5, 5]), 110)

    def test_asymmetric_digit_lengths(self):
        # [1, 10000] -> concat(1,10000) = 110000
        self.assertEqual(concatenationValue([1, 10000]), 110000)


if __name__ == "__main__":
    unittest.main()
