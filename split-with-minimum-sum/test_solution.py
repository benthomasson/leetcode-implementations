"""Tests for Split With Minimum Sum."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import min_sum_of_two_numbers


class TestMinSumOfTwoNumbers(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(min_sum_of_two_numbers(4325), 59)

    def test_example_2(self):
        self.assertEqual(min_sum_of_two_numbers(687), 75)

    def test_two_digit_min(self):
        self.assertEqual(min_sum_of_two_numbers(10), 1)

    def test_two_digit_no_zero(self):
        self.assertEqual(min_sum_of_two_numbers(98), 17)

    def test_repeated_digits(self):
        self.assertEqual(min_sum_of_two_numbers(1111), 22)

    def test_with_zeros(self):
        self.assertEqual(min_sum_of_two_numbers(2030), 5)

    def test_large_input(self):
        self.assertEqual(min_sum_of_two_numbers(999999999), 109998)

    def test_three_digits_ascending(self):
        self.assertEqual(min_sum_of_two_numbers(123), 15)

    def test_all_same_even_count(self):
        self.assertEqual(min_sum_of_two_numbers(55), 10)


if __name__ == "__main__":
    unittest.main()
