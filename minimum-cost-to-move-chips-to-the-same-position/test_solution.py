import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import sort_array


def test_example_1():
    assert sort_array([1, 2, 3]) == 1

def test_example_2():
    assert sort_array([2, 2, 2, 3, 3]) == 2

def test_example_3():
    assert sort_array([1, 1000000000]) == 1

def test_single_chip():
    assert sort_array([5]) == 0

def test_all_even():
    assert sort_array([2, 4, 6]) == 0

def test_all_odd():
    assert sort_array([1, 3, 5]) == 0

def test_one_odd_one_even():
    assert sort_array([1, 2]) == 1

def test_equal_odd_even():
    assert sort_array([1, 2, 3, 4]) == 2

def test_large_values_same_parity():
    assert sort_array([1000000000, 2, 4]) == 0


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
