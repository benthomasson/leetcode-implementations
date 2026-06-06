import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Simulate smashing heaviest stones using a max-heap.

        Args:
            stones: List of stone weights.

        Returns:
            Weight of the last remaining stone, or 0 if none remain.
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0
