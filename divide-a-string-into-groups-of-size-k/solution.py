from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """Divide a string into groups of size k, padding the last group with fill.

        Args:
            s: The input string to divide.
            k: The size of each group.
            fill: The character used to pad the last group.

        Returns:
            A list of strings, each of length k.
        """
        s += fill * ((k - len(s) % k) % k)
        return [s[i:i + k] for i in range(0, len(s), k)]
