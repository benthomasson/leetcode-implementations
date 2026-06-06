import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import Solution


class TestCanThreePartsEqualSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertTrue(self.s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))

    def test_example2(self):
        self.assertFalse(self.s.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))

    def test_example3(self):
        self.assertTrue(self.s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))

    # --- Edge cases ---
    def test_min_length_true(self):
        self.assertTrue(self.s.canThreePartsEqualSum([1, 1, 1]))

    def test_min_length_false(self):
        self.assertFalse(self.s.canThreePartsEqualSum([1, 2, 3]))

    def test_all_zeros(self):
        self.assertTrue(self.s.canThreePartsEqualSum([0, 0, 0, 0, 0]))

    def test_sum_not_divisible_by_3(self):
        self.assertFalse(self.s.canThreePartsEqualSum([1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(self.s.canThreePartsEqualSum([-3, -3, -3]))

    def test_partition_at_boundaries(self):
        # [10, 10, 10] -> each part is one element
        self.assertTrue(self.s.canThreePartsEqualSum([10, 10, 10]))

    def test_sum_zero_not_partitionable(self):
        # Sum is 0 but only two natural partitions: [1, -1, 1, -1] can't make 3 parts summing to 0?
        # Actually: [1] sum=1 != 0. So False.
        self.assertFalse(self.s.canThreePartsEqualSum([1, -1, 1, -1]))


if __name__ == '__main__':
    unittest.main()
