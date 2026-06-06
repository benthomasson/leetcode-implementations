"""Teemo Attacking - LeetCode Problem."""


def find_poisoned_duration(timeSeries: list[int], duration: int) -> int:
    """Calculate total seconds Ashe is poisoned by Teemo's attacks.

    Args:
        timeSeries: Non-decreasing list of attack timestamps.
        duration: Duration of each poison effect in seconds.

    Returns:
        Total number of seconds Ashe is poisoned.
    """
    if not timeSeries or duration == 0:
        return 0

    total = 0
    for i in range(len(timeSeries) - 1):
        total += min(timeSeries[i + 1] - timeSeries[i], duration)
    total += duration

    return total
