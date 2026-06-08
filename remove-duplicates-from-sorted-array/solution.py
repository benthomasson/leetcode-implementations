from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Remove duplicates from sorted array in-place, return count of unique elements.

        Args:
            nums: Sorted integer array (modified in-place).

        Returns:
            Number of unique elements.
        """
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k
