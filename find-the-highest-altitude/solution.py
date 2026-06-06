"""Find the highest altitude along a biker's road trip."""


def min_operations(gain: list[int]) -> int:
    """Find the highest altitude reached during a road trip.

    Args:
        gain: Net altitude gains between consecutive points.

    Returns:
        The highest altitude reached.
    """
    max_alt = alt = 0
    for g in gain:
        alt += g
        if alt > max_alt:
            max_alt = alt
    return max_alt
