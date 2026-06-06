def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    """Find the nearest valid point that shares the same x or y coordinate.

    Args:
        x: Current x-coordinate.
        y: Current y-coordinate.
        points: List of [ai, bi] coordinate pairs.

    Returns:
        Index of the nearest valid point, or -1 if none exist.
    """
    min_dist = float('inf')
    min_idx = -1
    for i, (ai, bi) in enumerate(points):
        if ai == x or bi == y:
            dist = abs(x - ai) + abs(y - bi)
            if dist < min_dist:
                min_dist = dist
                min_idx = i
    return min_idx
