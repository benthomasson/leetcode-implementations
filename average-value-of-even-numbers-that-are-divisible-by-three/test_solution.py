"""Tests for average_even_divisible_by_three."""

import unittest
from solution import average_even_divisible_by_three


class TestAverageEvenDivisibleByThree(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(average_even_divisible_by_three([1, 3, 6, 10, 12, 15]), 9)

    def test_example_2(self):
        self.assertEqual(average_even_divisible_by_three([1, 2, 4, 7, 10]), 0)

    def test_all_qualifying(self):
        self.assertEqual(average_even_divisible_by_three([6, 12, 18]), 12)

    def test_single_qualifying(self):
        self.assertEqual(average_even_divisible_by_three([6]), 6)

    def test_single_non_qualifying(self):
        self.assertEqual(average_even_divisible_by_three([5]), 0)

    def test_floor_division(self):
        # sum=6+18+30+42=96, count=4, 96//4=24
        self.assertEqual(average_even_divisible_by_three([6, 18, 30, 42]), 24)

    def test_boundary_values(self):
        self.assertEqual(average_even_divisible_by_three([1]), 0)
        self.assertEqual(average_even_divisible_by_three([996]), 996)

    def test_even_but_not_divisible_by_three(self):
        self.assertEqual(average_even_divisible_by_three([2, 4, 8, 10]), 0)

    def test_odd_divisible_by_three(self):
        self.assertEqual(average_even_divisible_by_three([3, 9, 15, 21]), 0)


if __name__ == "__main__":
    unittest.main()
