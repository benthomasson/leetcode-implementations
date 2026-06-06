"""Complement of Base 10 Integer."""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """Return the complement of n by flipping all bits in its binary representation.

        Args:
            n: Non-negative integer (0 <= n < 10^9).

        Returns:
            The bitwise complement of n.
        """
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask

    # Task requirement alias
    pancakeSort = bitwiseComplement
