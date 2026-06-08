from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """Return count of arr1 elements where no arr2 element is within distance d.

        Args:
            arr1: First integer array.
            arr2: Second integer array.
            d: Distance threshold.

        Returns:
            Number of elements in arr1 with no arr2 element within distance d.
        """
        arr2 = sorted(arr2)
        count = 0
        for val in arr1:
            pos = bisect_left(arr2, val)
            # Check closest neighbors: arr2[pos-1] (left) and arr2[pos] (right)
            too_close = False
            if pos < len(arr2) and abs(arr2[pos] - val) <= d:
                too_close = True
            if pos > 0 and abs(arr2[pos - 1] - val) <= d:
                too_close = True
            if not too_close:
                count += 1
        return count
