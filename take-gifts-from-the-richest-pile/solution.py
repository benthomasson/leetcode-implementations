"""Solution for LeetCode: Take Gifts From the Richest Pile."""

import heapq
import math


def giftsRemaining(gifts: list[int], k: int) -> int:
    """Return total gifts remaining after k seconds of taking from the richest pile.

    Args:
        gifts: Number of gifts in each pile.
        k: Number of seconds to take gifts.

    Returns:
        Total number of gifts remaining.
    """
    heap = [-g for g in gifts]
    heapq.heapify(heap)

    for _ in range(k):
        max_val = -heapq.heappop(heap)
        heapq.heappush(heap, -math.isqrt(max_val))

    return -sum(heap)
