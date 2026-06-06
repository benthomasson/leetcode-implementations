"""Tests for path crossing solution."""

import unittest
from solution import path_crossing


class TestPathCrossing(unittest.TestCase):

    def test_no_crossing(self):
        self.assertFalse(path_crossing("NES"))

    def test_crosses_origin(self):
        self.assertTrue(path_crossing("NESWW"))

    def test_single_step(self):
        self.assertFalse(path_crossing("N"))

    def test_return_to_origin(self):
        self.assertTrue(path_crossing("NESW"))

    def test_straight_line(self):
        self.assertFalse(path_crossing("NNNN"))

    def test_immediate_backtrack(self):
        self.assertTrue(path_crossing("NS"))

    def test_square_no_revisit(self):
        self.assertFalse(path_crossing("NES"))

    def test_long_non_crossing(self):
        self.assertFalse(path_crossing("NNNNEEEE"))

    def test_figure_eight_crosses(self):
        self.assertTrue(path_crossing("NESWNESW"))


if __name__ == "__main__":
    unittest.main()
