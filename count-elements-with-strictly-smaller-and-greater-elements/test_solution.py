import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import min_moves


def test_example1():
    assert min_moves([11, 7, 2, 15]) == 2

def test_example2():
    assert min_moves([-3, 3, 3, 90]) == 2

def test_single_element():
    assert min_moves([5]) == 0

def test_two_elements():
    assert min_moves([1, 2]) == 0

def test_all_same():
    assert min_moves([3, 3, 3]) == 0

def test_duplicates_at_boundaries():
    assert min_moves([1, 1, 2, 2]) == 0

def test_negative_numbers():
    assert min_moves([-5, -3, -1]) == 1

def test_multiple_middle():
    assert min_moves([1, 2, 2, 2, 3]) == 3

def test_large_range():
    assert min_moves([-100000, 0, 100000]) == 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
