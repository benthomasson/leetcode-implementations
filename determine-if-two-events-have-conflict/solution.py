"""Determine if two events have a conflict."""

from typing import List


def has_event_conflict(event1: List[str], event2: List[str]) -> bool:
    """Determine if two events on the same day have a time conflict.

    Args:
        event1: [startTime1, endTime1] in HH:MM format.
        event2: [startTime2, endTime2] in HH:MM format.

    Returns:
        True if the events overlap, False otherwise.
    """
    return event1[0] <= event2[1] and event2[0] <= event1[1]
