from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """Check if all 1's in nums are at least k places apart.

        Args:
            nums: Binary array of 0s and 1s.
            k: Minimum required distance between any two 1s.

        Returns:
            True if all 1s are at least k places apart, False otherwise.
        """
        last = -1
        for i, num in enumerate(nums):
            if num == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        return True
