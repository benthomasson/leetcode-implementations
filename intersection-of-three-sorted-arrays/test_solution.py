import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import Solution


class TestArraysIntersection(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]), [1,5])

    def test_example2_no_overlap(self):
        self.assertEqual(self.sol.arraysIntersection([197,418,523,876,1356], [501,880,1593,1710,1870], [521,682,1337,1395,1764]), [])

    def test_single_element_match(self):
        self.assertEqual(self.sol.arraysIntersection([1], [1], [1]), [1])

    def test_single_element_no_match(self):
        self.assertEqual(self.sol.arraysIntersection([1], [2], [3]), [])

    def test_all_identical(self):
        self.assertEqual(self.sol.arraysIntersection([1,2,3], [1,2,3], [1,2,3]), [1,2,3])

    def test_match_only_at_start(self):
        self.assertEqual(self.sol.arraysIntersection([1,2,3], [1,4,5], [1,6,7]), [1])

    def test_match_only_at_end(self):
        self.assertEqual(self.sol.arraysIntersection([1,2,5], [3,4,5], [4,5,6]), [5])

    def test_different_lengths(self):
        self.assertEqual(self.sol.arraysIntersection([1,2,3,4,5,6], [2,4], [2,4,6,8]), [2,4])

    def test_completely_disjoint(self):
        self.assertEqual(self.sol.arraysIntersection([1,2], [3,4], [5,6]), [])


if __name__ == '__main__':
    unittest.main()
