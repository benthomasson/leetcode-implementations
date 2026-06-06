from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """Check if an array is monotonic (non-decreasing or non-increasing).

        Args:
            nums: List of integers.

        Returns:
            True if the array is monotonic, False otherwise.
        """
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            if nums[i] < nums[i + 1]:
                decreasing = False

        return increasing or decreasing
