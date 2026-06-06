def findShortestSubArray(nums: list[int]) -> int:
    """Find shortest subarray with same degree as the full array.

    Args:
        nums: Non-empty list of non-negative integers.

    Returns:
        Length of the shortest contiguous subarray with the same degree.
    """
    count: dict[int, int] = {}
    first: dict[int, int] = {}
    last: dict[int, int] = {}

    for i, n in enumerate(nums):
        if n not in first:
            first[n] = i
        last[n] = i
        count[n] = count.get(n, 0) + 1

    degree = max(count.values())
    return min(last[n] - first[n] + 1 for n, c in count.items() if c == degree)
