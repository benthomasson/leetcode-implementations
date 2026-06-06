"""Sort Even and Odd Indices Independently."""


def maxValue(nums: list[int]) -> list[int]:
    """Sort even indices ascending and odd indices descending, then interleave.

    Args:
        nums: 0-indexed integer array.

    Returns:
        Array with even-indexed values sorted non-decreasing and
        odd-indexed values sorted non-increasing.
    """
    evens = sorted(nums[::2])
    odds = sorted(nums[1::2], reverse=True)

    result = []
    for i in range(len(nums)):
        result.append(evens[i // 2] if i % 2 == 0 else odds[i // 2])
    return result
