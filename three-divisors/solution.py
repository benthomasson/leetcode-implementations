import math


class Solution:
    def isThreeDivisors(self, n: int) -> bool:
        """Return True if n has exactly three positive divisors.

        Args:
            n: A positive integer (1 <= n <= 10^4).

        Returns:
            True if n has exactly three divisors, False otherwise.
        """
        sqrt = int(math.isqrt(n))
        if sqrt * sqrt != n:
            return False
        # Check if sqrt is prime
        if sqrt < 2:
            return False
        for i in range(2, int(math.isqrt(sqrt)) + 1):
            if sqrt % i == 0:
                return False
        return True
