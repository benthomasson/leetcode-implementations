from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """Find indices where target appears after sorting nums.

        Args:
            nums: Integer array to sort and search.
            target: Value to find indices for.

        Returns:
            Sorted list of indices where target appears in sorted nums.
        """
        left = sum(1 for x in nums if x < target)
        count = sum(1 for x in nums if x == target)
        return list(range(left, left + count))
