from typing import List


class Solution:
    def maxSideLength(self, nums: List[int]) -> int:
        """Find minimum positive startValue so step-by-step sum is always >= 1.

        Args:
            nums: Array of integers to sum step by step.

        Returns:
            Minimum positive startValue.
        """
        min_sum = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            min_sum = min(min_sum, running_sum)
        return max(1, 1 - min_sum)
