"""Decode XORed Array - LeetCode Solution."""

import unittest
from typing import List


class Solution:
    def minOperations(self, encoded: List[int], first: int) -> List[int]:
        """Decode an XOR-encoded array given the first element.

        Args:
            encoded: XOR-encoded array where encoded[i] = arr[i] ^ arr[i+1].
            first: The first element of the original array.

        Returns:
            The original decoded array.
        """
        arr = [first]
        for val in encoded:
            arr.append(arr[-1] ^ val)
        return arr


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minOperations([1, 2, 3], 1), [1, 0, 2, 1])

    def test_example2(self):
        self.assertEqual(self.s.minOperations([6, 2, 7, 3], 4), [4, 2, 0, 7, 4])

    def test_single_encoded(self):
        self.assertEqual(self.s.minOperations([5], 3), [3, 6])

    def test_all_zeros(self):
        self.assertEqual(self.s.minOperations([0, 0, 0], 0), [0, 0, 0, 0])

    def test_first_zero(self):
        self.assertEqual(self.s.minOperations([7], 0), [0, 7])

    def test_large_values(self):
        self.assertEqual(self.s.minOperations([100000], 100000), [100000, 0])


if __name__ == "__main__":
    unittest.main()
