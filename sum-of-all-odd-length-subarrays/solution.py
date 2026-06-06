from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """Return the sum of all odd-length subarrays of arr.

        For each element at index i in an array of length n, the number of
        odd-length subarrays containing it is ((i+1)*(n-i)+1)//2.

        Args:
            arr: Array of positive integers.

        Returns:
            Sum of all odd-length subarrays.
        """
        n = len(arr)
        return sum(arr[i] * (((i + 1) * (n - i) + 1) // 2) for i in range(n))
