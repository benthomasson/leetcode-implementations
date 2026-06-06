from collections import Counter


def countLargestGroup(n: int) -> int:
    """Count groups with the largest size when numbers 1..n are grouped by digit sum.

    Args:
        n: Upper bound of the range [1, n].

    Returns:
        Number of groups that have the largest size.
    """
    counts = Counter(sum(int(d) for d in str(i)) for i in range(1, n + 1))
    max_size = max(counts.values())
    return sum(1 for v in counts.values() if v == max_size)
