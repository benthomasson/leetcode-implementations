"""Tests for Remove Element solution."""

from solution import removeElement


def test_example1():
    nums = [3, 2, 2, 3]
    k = removeElement(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_example2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = removeElement(nums, 2)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]


def test_empty():
    nums = []
    assert removeElement(nums, 1) == 0


def test_all_match():
    nums = [2, 2, 2]
    assert removeElement(nums, 2) == 0


def test_no_match():
    nums = [1, 3, 5]
    k = removeElement(nums, 2)
    assert k == 3
    assert sorted(nums[:k]) == [1, 3, 5]


def test_single_match():
    nums = [1]
    assert removeElement(nums, 1) == 0


def test_single_no_match():
    nums = [1]
    k = removeElement(nums, 2)
    assert k == 1
    assert nums[0] == 1


def test_val_out_of_range():
    nums = [0, 1, 2]
    k = removeElement(nums, 100)
    assert k == 3
    assert sorted(nums[:k]) == [0, 1, 2]


def test_all_same_not_val():
    nums = [5, 5, 5, 5]
    k = removeElement(nums, 3)
    assert k == 4
    assert sorted(nums[:k]) == [5, 5, 5, 5]
