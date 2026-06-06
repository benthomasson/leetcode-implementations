"""Rank Transform of an Array - LeetCode 1331."""

from typing import List
import unittest


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """Replace each element with its dense rank.

        Args:
            arr: Array of integers.

        Returns:
            Array with each element replaced by its rank.
        """
        rank_map = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [rank_map[x] for x in arr]


class TestArrayRankTransform(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.arrayRankTransform([40, 10, 20, 30]), [4, 1, 2, 3])

    def test_example2(self):
        self.assertEqual(self.s.arrayRankTransform([100, 100, 100]), [1, 1, 1])

    def test_example3(self):
        self.assertEqual(
            self.s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]),
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
        )

    def test_empty(self):
        self.assertEqual(self.s.arrayRankTransform([]), [])

    def test_single(self):
        self.assertEqual(self.s.arrayRankTransform([42]), [1])

    def test_negatives(self):
        self.assertEqual(self.s.arrayRankTransform([-5, -10, 0]), [2, 1, 3])

    def test_already_sorted(self):
        self.assertEqual(self.s.arrayRankTransform([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_sorted(self):
        self.assertEqual(self.s.arrayRankTransform([4, 3, 2, 1]), [4, 3, 2, 1])

    def test_all_same(self):
        self.assertEqual(self.s.arrayRankTransform([7, 7, 7, 7, 7]), [1, 1, 1, 1, 1])

    def test_large_values(self):
        self.assertEqual(
            self.s.arrayRankTransform([-10**9, 10**9, 0]), [1, 3, 2]
        )


if __name__ == "__main__":
    unittest.main()
