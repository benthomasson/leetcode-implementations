from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        """Return the concatenation of nums with itself.

        Args:
            nums: Integer array of length n.

        Returns:
            Array of length 2n where ans[i] == ans[i+n] == nums[i].
        """
        return nums + nums
