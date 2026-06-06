from collections import Counter
from typing import List


class Solution:
    def sumOfUniqueElements(self, nums: List[int]) -> int:
        """Return the sum of elements that appear exactly once in nums.

        Args:
            nums: List of integers.

        Returns:
            Sum of unique elements.
        """
        return sum(val for val, cnt in Counter(nums).items() if cnt == 1)
