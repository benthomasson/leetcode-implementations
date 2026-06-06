"""Tests for merge-similar-items solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import sum_weights


class TestSumWeights(unittest.TestCase):
    # --- Problem examples ---
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

    # --- Edge cases ---
    def test_no_overlap(self):
        self.assertEqual(
            sum_weights([[1, 2]], [[3, 4]]),
            [[1, 2], [3, 4]],
        )

    def test_full_overlap(self):
        self.assertEqual(
            sum_weights([[1, 1], [2, 2]], [[1, 3], [2, 4]]),
            [[1, 4], [2, 6]],
        )

    def test_single_element_each(self):
        self.assertEqual(sum_weights([[5, 10]], [[5, 20]]), [[5, 30]])

    def test_boundary_max_values(self):
        self.assertEqual(
            sum_weights([[1000, 1000]], [[1000, 1000]]),
            [[1000, 2000]],
        )

    def test_boundary_min_values(self):
        self.assertEqual(sum_weights([[1, 1]], [[1, 1]]), [[1, 2]])

    def test_result_sorted(self):
        result = sum_weights([[9, 1], [1, 1]], [[5, 1]])
        values = [r[0] for r in result]
        self.assertEqual(values, sorted(values))

    def test_many_items_no_overlap(self):
        items1 = [[i, 1] for i in range(1, 501)]
        items2 = [[i, 1] for i in range(501, 1001)]
        result = sum_weights(items1, items2)
        self.assertEqual(len(result), 1000)
        self.assertEqual(result[0], [1, 1])
        self.assertEqual(result[-1], [1000, 1])


if __name__ == "__main__":
    unittest.main()
