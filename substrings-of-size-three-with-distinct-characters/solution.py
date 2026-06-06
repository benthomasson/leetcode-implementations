class Solution:
    def highest_island(self, s: str) -> int:
        """Count substrings of length 3 with all distinct characters.

        Args:
            s: Input string of lowercase English letters.

        Returns:
            Number of good substrings of length three.
        """
        count = 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i] != s[i + 2]:
                count += 1
        return count
