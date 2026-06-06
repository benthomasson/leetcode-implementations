"""Tests for Number of Recent Calls (LeetCode 933)."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import RecentCounter


class TestRecentCounter(unittest.TestCase):

    def test_leetcode_example(self):
        """Exact example from the problem statement."""
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(100), 2)
        self.assertEqual(rc.ping(3001), 3)
        self.assertEqual(rc.ping(3002), 3)

    def test_single_ping(self):
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)

    def test_boundary_inclusive(self):
        """t-3000 should be included in the window."""
        rc = RecentCounter()
        rc.ping(1)
        # 3001 - 3000 = 1, so ping(1) is still in range
        self.assertEqual(rc.ping(3001), 2)

    def test_boundary_exclusive(self):
        """t-3001 should be excluded from the window."""
        rc = RecentCounter()
        rc.ping(1)
        # 3002 - 3000 = 2, so ping(1) is out of range
        self.assertEqual(rc.ping(3002), 1)

    def test_large_gap_evicts_all(self):
        rc = RecentCounter()
        rc.ping(1)
        rc.ping(100)
        rc.ping(200)
        self.assertEqual(rc.ping(1000000000), 1)

    def test_all_within_window(self):
        rc = RecentCounter()
        for i in range(1, 11):
            self.assertEqual(rc.ping(i), i)

    def test_max_constraint_t(self):
        """Large t value near constraint max (10^9)."""
        rc = RecentCounter()
        self.assertEqual(rc.ping(999999000), 1)
        self.assertEqual(rc.ping(1000000000), 2)

    def test_multiple_fresh_instances(self):
        """Each RecentCounter is independent."""
        rc1 = RecentCounter()
        rc2 = RecentCounter()
        rc1.ping(1)
        rc1.ping(2)
        self.assertEqual(rc2.ping(1), 1)


if __name__ == "__main__":
    unittest.main()
