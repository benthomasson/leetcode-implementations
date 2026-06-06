from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """Find the missing number in an arithmetic progression.

        Args:
            arr: Array with one value removed from an arithmetic progression.

        Returns:
            The removed value.
        """
        n = len(arr)
        expected_diff = (arr[-1] - arr[0]) // n

        if expected_diff == 0:
            return arr[0]

        for i in range(n - 1):
            if arr[i + 1] - arr[i] != expected_diff:
                return arr[i] + expected_diff

        return arr[0]
