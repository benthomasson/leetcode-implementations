"""Max Consecutive Ones - LeetCode 485."""


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    """Return the maximum number of consecutive 1's in a binary array.

    Args:
        nums: Binary array where each element is 0 or 1.

    Returns:
        Maximum count of consecutive 1's.
    """
    max_streak = 0
    current = 0
    for n in nums:
        if n == 1:
            current += 1
            if current > max_streak:
                max_streak = current
        else:
            current = 0
    return max_streak
