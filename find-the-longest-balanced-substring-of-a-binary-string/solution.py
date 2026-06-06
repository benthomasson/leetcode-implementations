"""Find the longest balanced substring of a binary string."""


def longestBalancedSubstring(s: str) -> int:
    """Return the length of the longest balanced substring.

    A balanced substring has all zeros before ones with equal counts.

    Args:
        s: Binary string of '0's and '1's.

    Returns:
        Length of the longest balanced substring.
    """
    zeros = ones = best = 0
    for c in s:
        if c == '0':
            if ones > 0:
                zeros = 0
                ones = 0
            zeros += 1
        else:
            ones += 1
            best = max(best, 2 * min(zeros, ones))
    return best
