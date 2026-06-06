"""Minimum Time Visiting All Points."""


def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    """Return minimum seconds to visit all points in order.

    Args:
        points: List of [x, y] coordinates to visit in order.

    Returns:
        Minimum time in seconds to visit all points.
    """
    return sum(
        max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1]))
        for i in range(len(points) - 1)
    )
