from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        """Return n unique integers that sum to zero.

        Args:
            n: Number of unique integers to return.

        Returns:
            List of n unique integers summing to zero.
        """
        result = []
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        if n % 2 == 1:
            result.append(0)
        return result
