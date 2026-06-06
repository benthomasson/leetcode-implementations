class Solution:
    def thousand_separator(self, n: int) -> str:
        """Add dot as thousands separator to integer n.

        Args:
            n: Non-negative integer to format.

        Returns:
            String with dots as thousands separators.
        """
        s = str(n)
        chunks = []
        while len(s) > 3:
            chunks.append(s[-3:])
            s = s[:-3]
        chunks.append(s)
        return ".".join(reversed(chunks))
