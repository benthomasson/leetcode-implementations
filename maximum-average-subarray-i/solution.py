from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Find the contiguous subarray of length k with maximum average.

        Args:
            nums: List of integers.
            k: Length of the subarray.

        Returns:
            Maximum average value of any subarray of length k.
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k
