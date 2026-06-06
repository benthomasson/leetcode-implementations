"""Perfect Number - LeetCode"""

import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """Check if num is a perfect number.

        Args:
            num: Positive integer to check.

        Returns:
            True if num is a perfect number, False otherwise.
        """
        if num <= 1:
            return False

        divisor_sum = 1
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:
                    divisor_sum += num // i

        return divisor_sum == num
