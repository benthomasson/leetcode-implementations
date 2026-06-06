"""Meeting Rooms - LeetCode Problem."""


def can_attend_meetings(intervals: list[list[int]]) -> bool:
    """Determine if a person could attend all meetings.

    Args:
        intervals: List of [start, end] meeting time intervals.

    Returns:
        True if all meetings can be attended without overlap.
    """
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True
