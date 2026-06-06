from typing import List


def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str]:
    """Find missing ranges in a sorted array within [lower, upper].

    Args:
        nums: Sorted unique integers within [lower, upper].
        lower: Lower bound of the range.
        upper: Upper bound of the range.

    Returns:
        List of formatted range strings covering all missing numbers.
    """
    result = []
    next_expected = lower

    for num in nums:
        if num > next_expected:
            result.append(_format_range(next_expected, num - 1))
        next_expected = num + 1

    if next_expected <= upper:
        result.append(_format_range(next_expected, upper))

    return result


def _format_range(a: int, b: int) -> str:
    return str(a) if a == b else f"{a}->{b}"
