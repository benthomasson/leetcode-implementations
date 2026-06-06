"""Tests for maximum ascending subarray sum."""

import unittest
from solution import concatenated_binary


class TestMaxAscendingSum(unittest.TestCase):
    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(concatenated_binary([10, 20, 30, 5, 10, 50]), 65)

    def test_example2(self):
        self.assertEqual(concatenated_binary([10, 20, 30, 40, 50]), 150)

    def test_example3(self):
        self.assertEqual(concatenated_binary([12, 17, 15, 13, 10, 11, 12]), 33)

    # --- Edge cases ---
    def test_single_element(self):
        self.assertEqual(concatenated_binary([42]), 42)

    def test_all_equal(self):
        self.assertEqual(concatenated_binary([5, 5, 5]), 5)

    def test_all_descending(self):
        self.assertEqual(concatenated_binary([30, 20, 10]), 30)

    def test_two_ascending(self):
        self.assertEqual(concatenated_binary([1, 2]), 3)

    def test_two_descending(self):
        self.assertEqual(concatenated_binary([2, 1]), 2)

    # --- Additional coverage ---
    def test_max_subarray_at_end(self):
        self.assertEqual(concatenated_binary([1, 2, 1, 2, 3]), 6)

    def test_max_subarray_at_start(self):
        self.assertEqual(concatenated_binary([10, 20, 30, 1, 2]), 60)


if __name__ == "__main__":
    unittest.main()
