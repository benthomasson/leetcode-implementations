class Solution:
    def divisorGame(self, n: int) -> bool:
        """Alice wins the Divisor Game iff n is even.

        Args:
            n: Starting number on the chalkboard (1 <= n <= 1000).

        Returns:
            True if Alice wins assuming optimal play.
        """
        return n % 2 == 0

    mincostTickets = divisorGame
