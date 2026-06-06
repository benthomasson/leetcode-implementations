import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import find_k_distant_indices


def test_example_1():
    assert find_k_distant_indices([3, 4, 9, 1, 3, 9, 5], 9, 1) == [1, 2, 3, 4, 5, 6]


def test_example_2():
    assert find_k_distant_indices([2, 2, 2, 2, 2], 2, 2) == [0, 1, 2, 3, 4]


def test_single_element():
    assert find_k_distant_indices([5], 5, 1) == [0]


def test_key_at_start():
    assert find_k_distant_indices([9, 1, 1, 1, 1], 9, 2) == [0, 1, 2]


def test_key_at_end():
    assert find_k_distant_indices([1, 1, 1, 1, 9], 9, 2) == [2, 3, 4]


def test_no_overlap():
    assert find_k_distant_indices([9, 1, 1, 1, 1, 9], 9, 1) == [0, 1, 4, 5]


def test_k_covers_whole_array():
    assert find_k_distant_indices([1, 2, 3, 9, 5], 9, 10) == [0, 1, 2, 3, 4]


def test_overlapping_ranges():
    assert find_k_distant_indices([9, 1, 9], 9, 1) == [0, 1, 2]


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
