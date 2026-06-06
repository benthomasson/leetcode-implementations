class Solution:
    def maximumRemovals(self, s: str) -> int:
        """Return minimum moves to convert all characters to 'O'.

        Args:
            s: String of 'X' and 'O' characters.

        Returns:
            Minimum number of 3-character moves needed.
        """
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves
