from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """Build array where ans[i] = nums[nums[i]] using O(1) extra space.

        Args:
            nums: Zero-based permutation of integers 0 to len(nums)-1.

        Returns:
            Array where each element is nums[nums[i]].
        """
        n = len(nums)
        # Encode: nums[i] = original + n * new_value
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        # Decode: extract new_value
        for i in range(n):
            nums[i] //= n
        return nums
