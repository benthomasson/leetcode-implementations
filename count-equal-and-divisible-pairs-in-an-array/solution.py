"""Count Equal and Divisible Pairs in an Array."""

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """Count pairs (i,j) where nums[i]==nums[j] and (i*j)%k==0.

        Args:
            nums: 0-indexed integer array.
            k: Divisor for the index product check.

        Returns:
            Number of valid pairs.
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count


def min_months(nums: List[int], k: int) -> int:
    """Wrapper matching required function name."""
    return Solution().countPairs(nums, k)
