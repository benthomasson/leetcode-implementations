"""LeetCode 989: Add to Array-Form of Integer."""

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """Return array-form of num + k.

        Args:
            num: Array-form of an integer.
            k: Integer to add.

        Returns:
            Array-form of the sum.
        """
        i = len(num) - 1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
            else:
                num.insert(0, k % 10)
            k //= 10
            i -= 1
        return num


import unittest


class TestAddToArrayForm(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.addToArrayForm([1, 2, 0, 0], 34), [1, 2, 3, 4])

    def test_example2(self):
        self.assertEqual(self.s.addToArrayForm([2, 7, 4], 181), [4, 5, 5])

    def test_example3(self):
        self.assertEqual(self.s.addToArrayForm([2, 1, 5], 806), [1, 0, 2, 1])

    def test_single_digit(self):
        self.assertEqual(self.s.addToArrayForm([5], 3), [8])

    def test_carry_overflow(self):
        self.assertEqual(self.s.addToArrayForm([9, 9, 9], 1), [1, 0, 0, 0])

    def test_zero_array(self):
        self.assertEqual(self.s.addToArrayForm([0], 100), [1, 0, 0])

    def test_k_much_larger(self):
        self.assertEqual(self.s.addToArrayForm([1], 9999), [1, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
