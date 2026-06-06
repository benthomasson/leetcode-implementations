"""Make Array Zero by Subtracting Equal Amounts."""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """Return minimum operations to make all elements zero.

        Args:
            nums: Non-negative integer array.

        Returns:
            Count of operations needed.
        """
        return len(set(nums) - {0})
