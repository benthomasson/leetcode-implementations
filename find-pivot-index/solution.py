from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Find the leftmost pivot index where left sum equals right sum.

        Args:
            nums: Array of integers.

        Returns:
            The leftmost pivot index, or -1 if none exists.
        """
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1
