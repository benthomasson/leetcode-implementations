from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """Find integers appearing in all three sorted arrays using three pointers.

        Args:
            arr1: Sorted array of integers in strictly increasing order.
            arr2: Sorted array of integers in strictly increasing order.
            arr3: Sorted array of integers in strictly increasing order.

        Returns:
            Sorted list of integers present in all three arrays.
        """
        result = []
        i = j = k = 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                i += 1
            elif arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1
        return result
