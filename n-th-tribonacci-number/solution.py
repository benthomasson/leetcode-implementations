"""N-th Tribonacci Number."""


class Solution:
    def tribonacci(self, n: int) -> int:
        """Return the n-th Tribonacci number.

        Args:
            n: Index in the Tribonacci sequence (0 <= n <= 37).

        Returns:
            The n-th Tribonacci number.
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
