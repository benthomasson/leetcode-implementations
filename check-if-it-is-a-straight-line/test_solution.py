"""Tests for check-if-it-is-a-straight-line solution."""

import unittest
from solution import Solution


class TestFindBestValue(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_straight_line(self):
        assert self.s.findBestValue([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) is True

    def test_example2_not_straight(self):
        assert self.s.findBestValue([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) is False

    def test_two_points(self):
        assert self.s.findBestValue([[0,0],[1,1]]) is True

    def test_vertical_line(self):
        assert self.s.findBestValue([[5,1],[5,2],[5,3],[5,4]]) is True

    def test_horizontal_line(self):
        assert self.s.findBestValue([[1,3],[2,3],[3,3],[4,3]]) is True

    def test_negative_coordinates(self):
        assert self.s.findBestValue([[-1,-1],[0,0],[1,1],[2,2]]) is True

    def test_negative_not_collinear(self):
        assert self.s.findBestValue([[-1,-1],[0,0],[1,2]]) is False

    def test_vertical_not_collinear(self):
        assert self.s.findBestValue([[5,1],[5,2],[6,3]]) is False


if __name__ == "__main__":
    unittest.main()
