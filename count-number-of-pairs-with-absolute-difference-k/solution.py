"""Solution for LeetCode: Count Number of Pairs With Absolute Difference K."""

from collections import Counter


def chalk_replacer(nums: list[int], k: int) -> int:
    """Count pairs (i, j) where i < j and |nums[i] - nums[j]| == k.

    Uses a frequency counter to achieve O(n) time complexity. For each unique
    value v, pairs where one element is v and the other is v + k are counted
    as count[v] * count[v + k].

    Args:
        nums: List of integers (1 <= nums[i] <= 100).
        k: Target absolute difference (1 <= k <= 99).

    Returns:
        Number of valid pairs with absolute difference equal to k.

    Examples:
        >>> chalk_replacer([1, 2, 2, 1], 1)
        4
        >>> chalk_replacer([1, 3], 3)
        0
        >>> chalk_replacer([3, 2, 1, 5, 4], 2)
        3
    """
    freq = Counter(nums)
    result = 0
    for v in freq:
        if v + k in freq:
            result += freq[v] * freq[v + k]
    return result
