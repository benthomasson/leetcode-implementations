"""Tests for Distance Between Bus Stops solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestDistanceBetweenBusStops(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().distanceBetweenBusStops

    # Problem examples
    def test_example1(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 0, 1), 1)

    def test_example2(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 0, 2), 3)

    def test_example3(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 0, 3), 4)

    # Edge cases
    def test_same_stop(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 2, 2), 0)

    def test_start_greater_than_destination(self):
        self.assertEqual(self.solve([1, 2, 3, 4], 3, 0), 4)

    def test_single_stop(self):
        self.assertEqual(self.solve([5], 0, 0), 0)

    def test_two_stops_shorter_first(self):
        self.assertEqual(self.solve([1, 2], 0, 1), 1)

    def test_adjacent_last_to_first(self):
        # Going from stop 3 to stop 0 via the wrap-around edge (distance[3]=4)
        self.assertEqual(self.solve([1, 2, 3, 4], 3, 0), 4)

    def test_large_distances(self):
        self.assertEqual(self.solve([10000, 10000, 10000], 0, 1), 10000)

    def test_asymmetric_distances(self):
        # [1, 100, 1, 1] stops 0-3: clockwise 0->1->2->3 = 102, counter = 1
        self.assertEqual(self.solve([1, 100, 1, 1], 0, 3), 1)


if __name__ == "__main__":
    unittest.main()
