import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution

import pytest


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    image = [[1,1,1],[1,1,0],[1,0,1]]
    assert sol.floodFill(image, 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]


def test_example2_noop_same_color(sol):
    image = [[0,0,0],[0,0,0]]
    assert sol.floodFill(image, 0, 0, 0) == [[0,0,0],[0,0,0]]


def test_single_pixel(sol):
    assert sol.floodFill([[5]], 0, 0, 3) == [[3]]


def test_single_pixel_noop(sol):
    assert sol.floodFill([[5]], 0, 0, 5) == [[5]]


def test_full_grid_same_color(sol):
    image = [[1,1],[1,1]]
    assert sol.floodFill(image, 0, 0, 2) == [[2,2],[2,2]]


def test_no_spread_different_neighbors(sol):
    image = [[1,2],[3,4]]
    assert sol.floodFill(image, 0, 0, 9) == [[9,2],[3,4]]


def test_l_shaped_region(sol):
    image = [[1,1,0],[1,0,0],[1,1,1]]
    assert sol.floodFill(image, 0, 0, 5) == [[5,5,0],[5,0,0],[5,5,5]]


def test_corner_start(sol):
    image = [[0,1],[1,1]]
    assert sol.floodFill(image, 0, 0, 7) == [[7,1],[1,1]]
