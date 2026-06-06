"""Number of Recent Calls - LeetCode 933."""

from collections import deque
import unittest


class RecentCounter:
    """Counts requests within a 3000ms sliding window."""

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        """Adds request at time t, returns count in [t-3000, t].

        Args:
            t: Timestamp in milliseconds (strictly increasing).

        Returns:
            Number of requests in the past 3000ms window.
        """
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


class TestRecentCounter(unittest.TestCase):

    def test_example(self):
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(100), 2)
        self.assertEqual(rc.ping(3001), 3)
        self.assertEqual(rc.ping(3002), 3)

    def test_single_ping(self):
        rc = RecentCounter()
        self.assertEqual(rc.ping(5), 1)

    def test_all_within_window(self):
        rc = RecentCounter()
        for i in range(1, 11):
            self.assertEqual(rc.ping(i), i)

    def test_large_gap_evicts_all(self):
        rc = RecentCounter()
        rc.ping(1)
        rc.ping(2)
        self.assertEqual(rc.ping(10000), 1)

    def test_boundary_exactly_3000(self):
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(3001), 2)  # 3001 - 3000 = 1, inclusive
        self.assertEqual(rc.ping(3002), 2)  # 3002 - 3000 = 2, evicts 1


if __name__ == "__main__":
    unittest.main()
