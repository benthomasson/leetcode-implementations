from typing import List


class Solution:
    def sum_of_digits(self, nums: List[int]) -> int:
        """Return 0 if digit sum of min element is odd, 1 if even.

        Args:
            nums: Array of positive integers.

        Returns:
            0 if digit sum is odd, 1 if even.
        """
        min_val = min(nums)
        digit_sum = 0
        while min_val:
            digit_sum += min_val % 10
            min_val //= 10
        return 1 if digit_sum % 2 == 0 else 0
