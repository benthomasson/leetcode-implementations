"""Tests for Maximum Units on a Truck."""
import unittest
from solution import busiest_servers


class TestBusiestServers(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(busiest_servers([[1, 3], [2, 2], [3, 1]], 4), 8)

    def test_example_2(self):
        self.assertEqual(busiest_servers([[5, 10], [2, 5], [4, 7], [3, 9]], 10), 91)

    def test_single_box_type(self):
        self.assertEqual(busiest_servers([[5, 3]], 3), 9)

    def test_truck_larger_than_total_boxes(self):
        self.assertEqual(busiest_servers([[2, 3], [3, 2]], 10), 12)

    def test_truck_size_one(self):
        self.assertEqual(busiest_servers([[3, 5], [2, 1]], 1), 5)

    def test_all_same_units(self):
        self.assertEqual(busiest_servers([[2, 4], [3, 4], [1, 4]], 4), 16)


if __name__ == "__main__":
    unittest.main()
