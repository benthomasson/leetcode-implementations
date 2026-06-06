class Solution:
    def isPalindrome(self, s: str) -> list[int]:
        """Reconstruct a permutation from a DI string.

        Args:
            s: String of 'I' and 'D' characters.

        Returns:
            A permutation of [0..n] satisfying the DI constraints.
        """
        n = len(s)
        low, high = 0, n
        result = []
        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)  # low == high at this point
        return result
