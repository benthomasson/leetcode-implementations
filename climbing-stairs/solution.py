class Solution:
    def climbStairs(self, n: int) -> int:
        """Return the number of distinct ways to climb n stairs.

        Args:
            n: Number of stairs (1 <= n <= 45).

        Returns:
            Number of distinct ways to reach the top.
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
