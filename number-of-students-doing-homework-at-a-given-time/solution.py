"""Number of Students Doing Homework at a Given Time."""

import unittest
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """Count students doing homework at queryTime.

        Args:
            startTime: Start times for each student.
            endTime: End times for each student.
            queryTime: The time to query.

        Returns:
            Number of students where startTime[i] <= queryTime <= endTime[i].
        """
        return sum(1 for s, e in zip(startTime, endTime) if s <= queryTime <= e)


class TestBusyStudent(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.busyStudent([1, 2, 3], [3, 2, 7], 4), 1)

    def test_example2(self):
        self.assertEqual(self.sol.busyStudent([4], [4], 4), 1)

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


if __name__ == "__main__":
    unittest.main()
