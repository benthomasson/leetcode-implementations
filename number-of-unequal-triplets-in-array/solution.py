from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        """Count triplets (i,j,k) where all three values are pairwise distinct.

        Args:
            nums: List of positive integers.

        Returns:
            Number of valid triplets.
        """
        n = len(nums)
        result = 0
        left = 0
        for c in Counter(nums).values():
            right = n - left - c
            result += left * c * right
            left += c
        return result
