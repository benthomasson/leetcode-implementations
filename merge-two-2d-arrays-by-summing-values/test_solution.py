"""Tests for merge_nums."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import merge_nums
import unittest


class TestMergeNums(unittest.TestCase):

    def test_example1(self):
        assert merge_nums([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]) == [[1,6],[2,3],[3,2],[4,6]]

    def test_example2(self):
        assert merge_nums([[2,4],[3,6],[5,5]], [[1,3],[4,3]]) == [[1,3],[2,4],[3,6],[4,3],[5,5]]

    def test_no_overlap(self):
        assert merge_nums([[1,1],[3,3]], [[2,2],[4,4]]) == [[1,1],[2,2],[3,3],[4,4]]

    def test_complete_overlap(self):
        assert merge_nums([[1,1],[2,2]], [[1,3],[2,4]]) == [[1,4],[2,6]]

    def test_single_elements(self):
        assert merge_nums([[1,5]], [[1,10]]) == [[1,15]]
        assert merge_nums([[1,5]], [[2,10]]) == [[1,5],[2,10]]

    def test_one_array_longer(self):
        assert merge_nums([[1,1]], [[2,2],[3,3],[4,4]]) == [[1,1],[2,2],[3,3],[4,4]]

    def test_all_nums1_before_nums2(self):
        assert merge_nums([[1,1],[2,2]], [[5,5],[6,6]]) == [[1,1],[2,2],[5,5],[6,6]]

    def test_all_nums2_before_nums1(self):
        assert merge_nums([[5,5],[6,6]], [[1,1],[2,2]]) == [[1,1],[2,2],[5,5],[6,6]]

    def test_max_values(self):
        assert merge_nums([[1000,1000]], [[1000,1000]]) == [[1000,2000]]


if __name__ == '__main__':
    unittest.main()
