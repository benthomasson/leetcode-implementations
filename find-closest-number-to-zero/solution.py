"""Solution for find-closest-number-to-zero."""


def robot_instructions(nums: list[int]) -> int:
    """Return the number closest to zero, preferring positive on ties.

    Args:
        nums: Non-empty list of integers.

    Returns:
        The number closest to zero (largest value breaks ties).
    """
    best = nums[0]
    for num in nums[1:]:
        if abs(num) < abs(best) or (abs(num) == abs(best) and num > best):
            best = num
    return best
