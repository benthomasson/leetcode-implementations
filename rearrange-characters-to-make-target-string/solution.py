from collections import Counter


def maxNumberOfCopies(s: str, target: str) -> int:
    """Return max copies of target formable from letters in s.

    Args:
        s: Source string to take letters from.
        target: Target string to form copies of.

    Returns:
        Maximum number of complete copies of target.
    """
    s_count = Counter(s)
    t_count = Counter(target)
    return min(s_count[c] // t_count[c] for c in t_count)
