"""Generate a string with characters that have odd counts."""


class Solution:
    def generateTheString(self, n: int) -> str:
        """Return a string of length n where every character occurs an odd number of times.

        Args:
            n: Length of the string to generate (1 <= n <= 500).

        Returns:
            A string of lowercase letters with length n, each character appearing an odd number of times.
        """
        if n % 2 == 1:
            return "a" * n
        return "a" * (n - 1) + "b"
