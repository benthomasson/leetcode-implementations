from collections import Counter


def num_sub(nums: list[int]) -> list[int]:
    """Sort array by increasing frequency, breaking ties by decreasing value.

    Args:
        nums: Array of integers.

    Returns:
        Sorted array.
    """
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (freq[x], -x))
