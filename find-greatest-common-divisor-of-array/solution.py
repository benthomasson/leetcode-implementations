"""Find Greatest Common Divisor of Array - LeetCode #1979."""

from math import gcd
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """Return the GCD of the smallest and largest numbers in nums.

        Args:
            nums: List of positive integers (length >= 2).

        Returns:
            Greatest common divisor of min(nums) and max(nums).
        """
        return gcd(min(nums), max(nums))
