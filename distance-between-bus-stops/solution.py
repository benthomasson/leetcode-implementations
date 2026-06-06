"""Distance Between Bus Stops - LeetCode"""

from typing import List
import unittest


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """Return shortest distance between two stops on a circular bus route.

        Args:
            distance: Distance between consecutive stops (i and (i+1) % n).
            start: Starting stop index.
            destination: Destination stop index.

        Returns:
            Minimum distance between start and destination.
        """
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        return min(clockwise, sum(distance) - clockwise)


class TestDistanceBetweenBusStops(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().distanceBetweenBusStops

    def test_example1(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 0, 1), 1)

    def test_example2(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 0, 2), 3)

    def test_example3(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 0, 3), 4)

    def test_same_stop(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 2, 2), 0)

    def test_start_greater_than_destination(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 3, 0), 4)

    def test_single_stop(self):
        self.assertEqual(self.solve([5], 0, 0), 0)

    def test_all_zeros(self):
        self.assertEqual(self.solve([0, 0, 0], 0, 2), 0)

    def test_all_equal(self):
        self.assertEqual(self.solve([3, 3, 3, 3], 0, 2), 6)

    def test_two_stops(self):
        self.assertEqual(self.solve([1, 2], 0, 1), 1)


if __name__ == "__main__":
    unittest.main()
