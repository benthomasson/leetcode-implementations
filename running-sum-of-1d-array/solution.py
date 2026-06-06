from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Return the running sum of nums.

        Args:
            nums: Array of integers.

        Returns:
            The running sum array where result[i] = sum(nums[0]..nums[i]).
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
