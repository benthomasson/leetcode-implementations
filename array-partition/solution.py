"""Array Partition - LeetCode solution."""


def array_pair_sum(nums: list[int]) -> int:
    """Maximize sum of min(ai, bi) over n pairs from 2n integers.

    Args:
        nums: Array of 2n integers to pair up.

    Returns:
        Maximum possible sum of pair minimums.
    """
    nums.sort()
    return sum(nums[::2])
