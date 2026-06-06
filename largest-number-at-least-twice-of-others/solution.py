from typing import List


class Solution:
    def largestNumberAtLeastTwiceOfOthers(self, nums: List[int]) -> int:
        """Return index of largest element if it's at least twice all others, else -1.

        Args:
            nums: Integer array where the largest integer is unique.

        Returns:
            Index of the largest element if it's >= 2x every other element, else -1.
        """
        max_val = second_max = -1
        max_idx = 0

        for i, n in enumerate(nums):
            if n > max_val:
                second_max = max_val
                max_val = n
                max_idx = i
            elif n > second_max:
                second_max = n

        return max_idx if max_val >= 2 * second_max else -1
