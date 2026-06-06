from typing import List


class Solution:
    def minOperations(self, code: List[int], k: int) -> List[int]:
        """Decrypt circular array by summing next/previous k elements.

        Args:
            code: Circular array of integers.
            k: Number of neighbors to sum (positive=next, negative=previous, zero=replace with 0).

        Returns:
            Decrypted array.
        """
        n = len(code)
        if k == 0:
            return [0] * n
        result = []
        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            result.append(total)
        return result
