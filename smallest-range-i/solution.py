from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        """Return minimum score of nums after adding [-k, k] to each element at most once.

        Args:
            nums: Integer array.
            k: Maximum adjustment per element.

        Returns:
            Minimum possible difference between max and min of adjusted nums.
        """
        return max(0, max(nums) - min(nums) - 2 * k)
