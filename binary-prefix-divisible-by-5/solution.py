from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """Check divisibility by 5 for each binary prefix of nums.

        Args:
            nums: Binary array of 0s and 1s.

        Returns:
            List of booleans where answer[i] is True if the binary
            number formed by nums[0..i] is divisible by 5.
        """
        result = []
        remainder = 0
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            result.append(remainder == 0)
        return result
