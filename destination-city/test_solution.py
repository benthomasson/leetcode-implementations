"""Tests for the Destination City solution."""

import unittest

from solution import Solution


class TestDestinationCity(unittest.TestCase):
    """Tests for Solution.watched_videos_by_friends."""

    def setUp(self):
        self.sol = Solution()

    def test_example1_linear_chain(self):
        paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "Sao Paulo")

    def test_example2_unordered_paths(self):
        paths = [["B", "C"], ["D", "B"], ["C", "A"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "A")

    def test_example3_single_path(self):
        paths = [["A", "Z"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "Z")

    def test_cities_with_spaces(self):
        paths = [["New York ", "Los Angeles "], ["Los Angeles ", "San Francisco "]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "San Francisco ")

    def test_single_character_cities(self):
        paths = [["a", "b"], ["b", "c"], ["c", "d"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "d")

    def test_two_cities(self):
        paths = [["X", "Y"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "Y")

    def test_longer_chain(self):
        cities = list("ABCDEFGHIJ")
        paths = [[cities[i], cities[i + 1]] for i in range(len(cities) - 1)]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "J")

    def test_reversed_order_paths(self):
        """Paths given in reverse order of the actual route."""
        paths = [["C", "D"], ["B", "C"], ["A", "B"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "D")

    def test_empty_paths_raises(self):
        with self.assertRaises(ValueError):
            self.sol.watched_videos_by_friends([])

    def test_mixed_case_cities(self):
        paths = [["abc", "Xyz"], ["Xyz", "QRS"]]
        self.assertEqual(self.sol.watched_videos_by_friends(paths), "QRS")


if __name__ == "__main__":
    unittest.main()
