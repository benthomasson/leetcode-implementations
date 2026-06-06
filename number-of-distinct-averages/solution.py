"""Solution for LeetCode problem: Number of Distinct Averages."""


def distinctAverages(nums: list[int]) -> int:
    """Return the number of distinct averages from pairing min/max repeatedly.

    Args:
        nums: Even-length list of integers.

    Returns:
        Count of distinct averages.
    """
    nums.sort()
    sums = set()
    left, right = 0, len(nums) - 1
    while left < right:
        sums.add(nums[left] + nums[right])
        left += 1
        right -= 1
    return len(sums)
