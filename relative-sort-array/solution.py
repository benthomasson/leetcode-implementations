from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Sort arr1 so elements in arr2 appear first in arr2's order, rest ascending.

        Args:
            arr1: Array to sort.
            arr2: Array defining relative order.

        Returns:
            Sorted array.
        """
        count = Counter(arr1)
        result = []
        for x in arr2:
            result.extend([x] * count.pop(x))
        result.extend(sorted(count.elements()))
        return result
