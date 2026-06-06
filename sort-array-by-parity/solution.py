"""Sort Array By Parity - LeetCode 905."""

from typing import List
import unittest


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """Move all even integers before all odd integers in-place.

        Args:
            nums: Integer array with 1 <= len <= 5000, 0 <= nums[i] <= 5000.

        Returns:
            The array with evens before odds.
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums


class TestSortArrayByParity(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def _check(self, nums):
        result = self.s.sortArrayByParity(nums[:])
        evens = [x for x in result if x % 2 == 0]
        odds = [x for x in result if x % 2 == 1]
        self.assertEqual(result, evens + odds)
        self.assertEqual(sorted(result), sorted(nums))

    def test_example1(self):
        self._check([3, 1, 2, 4])

    def test_example2(self):
        self._check([0])

    def test_all_even(self):
        self._check([2, 4, 6, 8])

    def test_all_odd(self):
        self._check([1, 3, 5, 7])

    def test_single_odd(self):
        self._check([1])

    def test_already_sorted(self):
        self._check([2, 4, 1, 3])

    def test_reverse_sorted(self):
        self._check([1, 3, 2, 4])

    def test_same_value_even(self):
        self._check([2, 2, 2])

    def test_same_value_odd(self):
        self._check([3, 3, 3])

    def test_zeros(self):
        self._check([0, 0, 0])

    def test_boundary_values(self):
        self._check([0, 5000, 4999, 1])

    def test_two_elements(self):
        self._check([1, 2])
        self._check([2, 1])


if __name__ == "__main__":
    unittest.main()
