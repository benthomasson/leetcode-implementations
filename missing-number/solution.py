"""Missing Number - LeetCode Problem."""


def missingNumber(nums: list[int]) -> int:
    """Find the missing number in range [0, n].

    Args:
        nums: Array of n distinct numbers from range [0, n].

    Returns:
        The missing number from the range.
    """
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
