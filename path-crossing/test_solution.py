"""Tests for path crossing solution."""

import unittest
from solution import lucky_numbers


class TestLuckyNumbers(unittest.TestCase):

    def test_no_crossing(self):
        self.assertFalse(lucky_numbers("NES"))

    def test_crosses_origin(self):
        self.assertTrue(lucky_numbers("NESWW"))

    def test_single_step(self):
        self.assertFalse(lucky_numbers("N"))

    def test_return_to_origin(self):
        self.assertTrue(lucky_numbers("NESW"))

    def test_straight_line(self):
        self.assertFalse(lucky_numbers("NNNN"))

    def test_immediate_backtrack(self):
        self.assertTrue(lucky_numbers("NS"))

    def test_square_no_revisit(self):
        self.assertFalse(lucky_numbers("NES"))

    def test_long_non_crossing(self):
        self.assertFalse(lucky_numbers("NNNNEEEE"))

    def test_figure_eight_crosses(self):
        self.assertTrue(lucky_numbers("NESWNESW"))


if __name__ == "__main__":
    unittest.main()
