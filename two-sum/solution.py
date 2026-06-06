"""Two Sum problem solution."""


def twoSum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers that add up to target.

    Args:
        nums: List of integers.
        target: Target sum.

    Returns:
        List of two indices whose elements sum to target.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
