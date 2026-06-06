"""Third Maximum Number - LeetCode solution."""


def third_max(nums: list[int]) -> int:
    """Return the third distinct maximum in nums, or the maximum if it doesn't exist.

    Args:
        nums: Non-empty list of integers.

    Returns:
        The third distinct maximum, or the overall maximum if fewer than 3 distinct values.
    """
    first = second = third = None

    for n in nums:
        if n in (first, second, third):
            continue
        if first is None or n > first:
            first, second, third = n, first, second
        elif second is None or n > second:
            second, third = n, second
        elif third is None or n > third:
            third = n

    return third if third is not None else first
