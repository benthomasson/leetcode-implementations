import pytest
from solution import get_min_distance


def test_example_1():
    assert get_min_distance([1, 2, 3, 4, 5], 5, 3) == 1


def test_example_2():
    assert get_min_distance([1], 1, 0) == 0


def test_example_3():
    assert get_min_distance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0) == 0


def test_target_at_start():
    assert get_min_distance([5, 2, 3, 4, 5], 5, 0) == 0


def test_multiple_targets_closest_wins():
    assert get_min_distance([1, 3, 5, 3, 7], 3, 2) == 1


def test_target_before_and_after_start():
    assert get_min_distance([8, 2, 8, 4, 8], 8, 3) == 1


def test_start_at_end():
    assert get_min_distance([1, 2, 3, 4, 5], 1, 4) == 4


def test_large_array():
    nums = list(range(1, 501)) + [999] + list(range(501, 1001))
    assert get_min_distance(nums, 999, 500) == 0


def test_target_at_both_ends():
    assert get_min_distance([7, 2, 3, 4, 7], 7, 2) == 2


def test_start_at_beginning_target_at_end():
    assert get_min_distance([2, 3, 4, 5, 9], 9, 0) == 4
