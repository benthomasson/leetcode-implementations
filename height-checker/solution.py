"""Height Checker - LeetCode solution using counting sort."""


def height_checker(heights: list[int]) -> int:
    """Count indices where heights differ from sorted order.

    Args:
        heights: Current order of student heights (values 1-100).

    Returns:
        Number of indices where heights[i] != expected[i].
    """
    counts = [0] * 101
    for h in heights:
        counts[h] += 1

    mismatches = 0
    j = 1  # current height value in sorted order
    for h in heights:
        while counts[j] == 0:
            j += 1
        if h != j:
            mismatches += 1
        counts[j] -= 1
    return mismatches
