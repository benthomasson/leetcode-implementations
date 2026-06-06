"""Find Numbers with Even Number of Digits."""

from typing import List
import unittest


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """Return count of numbers with an even number of digits.

        Args:
            nums: List of positive integers.

        Returns:
            Count of integers that have an even number of digits.
        """
        return sum(1 for n in nums if len(str(n)) % 2 == 0)


class TestFindNumbers(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findNumbers([12, 345, 2, 6, 7896]), 2)

    def test_example2(self):
        self.assertEqual(self.s.findNumbers([555, 901, 482, 1771]), 1)

    def test_single_odd_digit(self):
        self.assertEqual(self.s.findNumbers([5]), 0)

    def test_single_even_digits(self):
        self.assertEqual(self.s.findNumbers([10]), 1)

    def test_all_even(self):
        self.assertEqual(self.s.findNumbers([12, 34, 56]), 3)

    def test_all_odd(self):
        self.assertEqual(self.s.findNumbers([1, 100, 10000]), 0)

    def test_boundary_100000(self):
        self.assertEqual(self.s.findNumbers([100000]), 1)


if __name__ == "__main__":
    unittest.main()
