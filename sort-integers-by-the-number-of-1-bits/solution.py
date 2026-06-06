from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """Sort integers by number of 1-bits, then by value.

        Args:
            arr: List of non-negative integers.

        Returns:
            Sorted list by bit count ascending, ties broken by value ascending.
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


# Alias per task spec
sort_integers_by_the_number_of_1_bits = Solution().sortByBits
