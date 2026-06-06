from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """Find the length of the longest continuous increasing subsequence.

        Args:
            nums: List of integers.

        Returns:
            Length of the longest strictly increasing contiguous subarray.
        """
        max_len = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 1
        return max_len
