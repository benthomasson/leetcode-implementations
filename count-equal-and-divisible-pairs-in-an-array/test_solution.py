"""Tests for count-equal-and-divisible-pairs-in-an-array."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution, min_months

import unittest


class TestCountPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        assert self.sol.countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4

    def test_example2(self):
        assert self.sol.countPairs([1, 2, 3, 4], 1) == 0

    def test_single_element(self):
        assert self.sol.countPairs([1], 1) == 0

    def test_all_same_k1(self):
        # All same, k=1: every pair counts. C(4,2) = 6
        assert self.sol.countPairs([5, 5, 5, 5], 1) == 6

    def test_all_same_large_k(self):
        # [1,1,1,1,1] k=6: pairs where i*j % 6 == 0
        # (0,1)=0✓ (0,2)=0✓ (0,3)=0✓ (0,4)=0✓ (2,3)=6✓ (3,4)=12✓ => 6
        assert self.sol.countPairs([1, 1, 1, 1, 1], 6) == 6

    def test_duplicates_but_no_divisible(self):
        # [2,1,2] k=100: pair (0,2) i*j=0 => 0%100=0 ✓ => 1
        assert self.sol.countPairs([2, 1, 2], 100) == 1

    def test_index_zero_always_divisible(self):
        # i=0 means i*j=0 which is divisible by any k
        assert self.sol.countPairs([7, 3, 7], 99) == 1

    def test_min_months_wrapper(self):
        assert min_months([3, 1, 2, 2, 2, 1, 3], 2) == 4
        assert min_months([1], 1) == 0


if __name__ == '__main__':
    unittest.main()
