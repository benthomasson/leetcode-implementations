from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """Count the number of good pairs (i, j) where nums[i] == nums[j] and i < j.

        Args:
            nums: List of integers.

        Returns:
            Number of good pairs.
        """
        count = 0
        seen = defaultdict(int)
        for num in nums:
            count += seen[num]
            seen[num] += 1
        return count
