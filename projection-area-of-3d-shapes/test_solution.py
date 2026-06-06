import sys
sys.path.insert(0, "../implementer")

from solution import Solution

s = Solution()


def test_example1():
    assert s.projectionArea([[1, 2], [3, 4]]) == 17


def test_example2():
    assert s.projectionArea([[2]]) == 5


def test_example3():
    assert s.projectionArea([[1, 0], [0, 2]]) == 8


def test_single_zero():
    # top=0, front=0, side=0
    assert s.projectionArea([[0]]) == 0


def test_all_zeros():
    assert s.projectionArea([[0, 0], [0, 0]]) == 0


def test_all_ones():
    # top=4, front=1+1=2, side=1+1=2 → 8
    assert s.projectionArea([[1, 1], [1, 1]]) == 8


def test_3x3_mixed():
    grid = [[1, 0, 3], [0, 5, 0], [2, 0, 1]]
    # top: 5 non-zero cells
    # front (row max): 3, 5, 2 → 10
    # side (col max): max(1,0,2)=2, max(0,5,0)=5, max(3,0,1)=3 → 10
    assert s.projectionArea(grid) == 25


def test_car_fleet_alias():
    assert s.carFleet([[2]]) == 5


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
