"""Merge Similar Items - LeetCode solution."""

from collections import defaultdict


def sum_weights(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    """Merge two item lists by summing weights for matching values.

    Args:
        items1: List of [value, weight] pairs with unique values.
        items2: List of [value, weight] pairs with unique values.

    Returns:
        Sorted list of [value, total_weight] pairs.
    """
    weights = defaultdict(int)
    for value, weight in items1:
        weights[value] += weight
    for value, weight in items2:
        weights[value] += weight
    return sorted([v, w] for v, w in weights.items())


import unittest


class TestSumWeights(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            sum_weights([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]),
            [[1, 6], [3, 9], [4, 5]],
        )

    def test_example2(self):
        self.assertEqual(
            sum_weights([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]),
            [[1, 4], [2, 4], [3, 4]],
        )

    def test_example3(self):
        self.assertEqual(
            sum_weights([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]),
            [[1, 7], [2, 4], [7, 1]],
        )

    def test_no_overlap(self):
        self.assertEqual(
            sum_weights([[1, 2]], [[3, 4]]),
            [[1, 2], [3, 4]],
        )

    def test_full_overlap(self):
        self.assertEqual(
            sum_weights([[1, 1]], [[1, 1]]),
            [[1, 2]],
        )

    def test_single_elements(self):
        self.assertEqual(
            sum_weights([[5, 10]], [[5, 20]]),
            [[5, 30]],
        )

    def test_boundary_values(self):
        self.assertEqual(
            sum_weights([[1000, 1000]], [[1000, 1000]]),
            [[1000, 2000]],
        )


if __name__ == "__main__":
    unittest.main()
