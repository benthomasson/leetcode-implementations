import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import pytest
from solution import Solution

s = Solution()

def test_example1():
    assert s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]) == pytest.approx(2.0)

def test_example2():
    assert s.largestTriangleArea([[1,0],[0,0],[0,1]]) == pytest.approx(0.5)

def test_collinear():
    assert s.largestTriangleArea([[0,0],[1,1],[2,2]]) == pytest.approx(0.0)

def test_negative_coords():
    assert s.largestTriangleArea([[-1,-1],[1,-1],[0,1]]) == pytest.approx(2.0)

def test_large_coords():
    assert s.largestTriangleArea([[50,50],[-50,-50],[50,-50]]) == pytest.approx(5000.0)

def test_minimum_input():
    assert s.largestTriangleArea([[0,0],[1,0],[0,1]]) == pytest.approx(0.5)

def test_unit_square_corners():
    assert s.largestTriangleArea([[0,0],[1,0],[1,1],[0,1]]) == pytest.approx(0.5)
