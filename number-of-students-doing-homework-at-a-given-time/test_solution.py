"""Tests for Number of Students Doing Homework at a Given Time."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestBusyStudent(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.sol.busyStudent([1, 2, 3], [3, 2, 7], 4), 1)

    def test_example2(self):
        self.assertEqual(self.sol.busyStudent([4], [4], 4), 1)

    # --- Edge cases ---
    def test_all_busy(self):
        self.assertEqual(self.sol.busyStudent([1, 1, 1], [5, 5, 5], 3), 3)

    def test_none_busy(self):
        self.assertEqual(self.sol.busyStudent([1, 2, 3], [3, 4, 5], 6), 0)

    def test_boundary_start(self):
        self.assertEqual(self.sol.busyStudent([5], [10], 5), 1)

    def test_boundary_end(self):
        self.assertEqual(self.sol.busyStudent([5], [10], 10), 1)

    def test_just_outside(self):
        self.assertEqual(self.sol.busyStudent([5], [10], 4), 0)
        self.assertEqual(self.sol.busyStudent([5], [10], 11), 0)

    def test_same_start_end(self):
        """Student starts and finishes at the same time, query matches."""
        self.assertEqual(self.sol.busyStudent([3], [3], 3), 1)

    def test_same_start_end_no_match(self):
        """Student starts and finishes at the same time, query doesn't match."""
        self.assertEqual(self.sol.busyStudent([3], [3], 4), 0)

    def test_max_constraints(self):
        """100 students, all doing homework from 1 to 1000."""
        start = [1] * 100
        end = [1000] * 100
        self.assertEqual(self.sol.busyStudent(start, end, 500), 100)


if __name__ == "__main__":
    unittest.main()
