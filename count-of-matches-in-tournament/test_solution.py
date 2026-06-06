"""Tests for Count of Matches in Tournament."""

import unittest
from solution import Solution


class TestNumberOfMatches(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_single_team(self):
        self.assertEqual(self.s.numberOfMatches(1), 0)

    def test_two_teams(self):
        self.assertEqual(self.s.numberOfMatches(2), 1)

    def test_odd_example(self):
        self.assertEqual(self.s.numberOfMatches(7), 6)

    def test_even_example(self):
        self.assertEqual(self.s.numberOfMatches(14), 13)

    def test_max_constraint(self):
        self.assertEqual(self.s.numberOfMatches(200), 199)


if __name__ == "__main__":
    unittest.main()
