from collections import Counter


def largest_unique_number(nums: list[int]) -> int:
    """Return the largest integer that occurs exactly once, or -1 if none.

    Args:
        nums: List of integers.

    Returns:
        Largest unique integer, or -1.
    """
    counts = Counter(nums)
    uniques = [n for n, c in counts.items() if c == 1]
    return max(uniques) if uniques else -1
