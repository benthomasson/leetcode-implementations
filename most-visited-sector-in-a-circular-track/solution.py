from typing import List


def most_visited_sector(n: int, rounds: List[int]) -> List[int]:
    """Find the most visited sectors on a circular track.

    Args:
        n: Number of sectors labeled 1 to n.
        rounds: Array where round i goes from rounds[i-1] to rounds[i].

    Returns:
        Most visited sector numbers in ascending order.
    """
    start, end = rounds[0], rounds[-1]
    if start <= end:
        return list(range(start, end + 1))
    return list(range(1, end + 1)) + list(range(start, n + 1))
