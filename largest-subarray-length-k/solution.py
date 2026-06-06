from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """Return the largest subarray of length k (lexicographic comparison).

        Args:
            nums: Array of distinct integers.
            k: Length of subarray.

        Returns:
            The lexicographically largest subarray of length k.
        """
        n = len(nums)
        max_idx = 0
        for i in range(1, n - k + 1):
            if nums[i] > nums[max_idx]:
                max_idx = i
        return nums[max_idx:max_idx + k]
