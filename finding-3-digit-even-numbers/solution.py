"""Finding 3-Digit Even Numbers - LeetCode Solution."""

from collections import Counter
from typing import List
import unittest


class Solution:
    def findThreeDigitEvenNumbers(self, digits: List[int]) -> List[int]:
        """Find all unique 3-digit even numbers formable from given digits.

        Args:
            digits: List of single digits (0-9), may contain duplicates.

        Returns:
            Sorted list of valid 3-digit even integers.
        """
        freq = Counter(digits)
        result = []
        for num in range(100, 999, 2):
            d1, rem = divmod(num, 100)
            d2, d3 = divmod(rem, 10)
            needed = Counter([d1, d2, d3])
            if all(freq[d] >= needed[d] for d in needed):
                result.append(num)
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.findThreeDigitEvenNumbers([2, 1, 3, 0]),
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.findThreeDigitEvenNumbers([2, 2, 8, 8, 2]),
            [222, 228, 282, 288, 822, 828, 882],
        )

    def test_example3(self):
        self.assertEqual(self.s.findThreeDigitEvenNumbers([3, 7, 5]), [])

    def test_all_zeros(self):
        self.assertEqual(self.s.findThreeDigitEvenNumbers([0, 0, 0]), [])

    def test_single_even_digit(self):
        self.assertEqual(self.s.findThreeDigitEvenNumbers([2, 2, 2]), [222])

    def test_min_length_valid(self):
        self.assertEqual(
            self.s.findThreeDigitEvenNumbers([1, 0, 2]),
            [102, 120, 210],
        )


if __name__ == "__main__":
    unittest.main()
