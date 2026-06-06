class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """Return the minimum number of bit flips to convert start to goal.

        Args:
            start: The starting integer.
            goal: The target integer.

        Returns:
            Number of bit positions where start and goal differ.
        """
        return bin(start ^ goal).count('1')
