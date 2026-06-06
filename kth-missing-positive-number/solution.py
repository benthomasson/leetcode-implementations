"""Kth Missing Positive Number - LeetCode #1539."""

from typing import List
import unittest


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """Find the kth missing positive integer from a sorted array.

        Args:
            arr: Sorted array of strictly increasing positive integers.
            k: The position of the missing number to find.

        Returns:
            The kth missing positive integer.
        """
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            # Number of missing positives before arr[mid] is arr[mid] - (mid + 1)
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid
        # At this point, left is the first index where missing count >= k
        # Answer is k + left
        return k + left


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findKthPositive([2, 3, 4, 7, 11], 5), 9)

    def test_example2(self):
        self.assertEqual(self.sol.findKthPositive([1, 2, 3, 4], 2), 6)

    def test_missing_before_array(self):
        # arr starts at 5, so 1,2,3,4 are missing; k=1 -> 1
        self.assertEqual(self.sol.findKthPositive([5, 6, 7], 1), 1)

    def test_no_gaps(self):
        # [1,2,3] has no gaps; k=1 -> 4
        self.assertEqual(self.sol.findKthPositive([1, 2, 3], 1), 4)

    def test_single_element(self):
        self.assertEqual(self.sol.findKthPositive([2], 1), 1)
        self.assertEqual(self.sol.findKthPositive([2], 2), 3)

    def test_large_k(self):
        self.assertEqual(self.sol.findKthPositive([1, 2, 3], 100), 103)

    def test_all_missing_at_start(self):
        # [10], k=3 -> 3
        self.assertEqual(self.sol.findKthPositive([10], 3), 3)


if __name__ == "__main__":
    unittest.main()
