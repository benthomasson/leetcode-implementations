from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        """Find intervals of consecutive character groups with 3+ characters.

        Args:
            s: String of lowercase English letters.

        Returns:
            List of [start, end] intervals for each large group.
        """
        result = []
        start = 0
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])
                start = i
        return result
