def sort_array(position: list[int]) -> int:
    """Find minimum cost to move all chips to the same position.

    Args:
        position: List of chip positions.

    Returns:
        Minimum cost to move all chips to one position.
    """
    odd = sum(p % 2 for p in position)
    return min(odd, len(position) - odd)
