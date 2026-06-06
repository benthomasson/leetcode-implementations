"""Count of Matches in Tournament."""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        """Return the number of matches played until a winner is decided.

        Args:
            n: Number of teams in the tournament.

        Returns:
            Total matches played.
        """
        return n - 1
