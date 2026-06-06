from typing import List


class Solution:
    def kids_with_candies(self, s: str, indices: List[int]) -> str:
        """Shuffle string by placing each character at its target index.

        Args:
            s: Input string to shuffle.
            indices: Target positions for each character.

        Returns:
            The shuffled string.
        """
        result = [''] * len(s)
        for i, idx in enumerate(indices):
            result[idx] = s[i]
        return ''.join(result)
