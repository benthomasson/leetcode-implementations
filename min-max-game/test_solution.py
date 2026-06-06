import sys
sys.path.insert(0, "../implementer")
from solution import min_steps


def test_example1():
    assert min_steps([1, 3, 5, 2, 4, 8, 2, 2]) == 1


def test_example2():
    assert min_steps([3]) == 3


def test_two_elements():
    # Single pair, even index → min
    assert min_steps([5, 2]) == 2


def test_four_elements():
    # i=0(even)→min(1,2)=1, i=1(odd)→max(3,4)=4 → [1,4]
    # i=0(even)→min(1,4)=1 → [1]
    assert min_steps([1, 2, 3, 4]) == 1


def test_all_identical():
    assert min_steps([7, 7, 7, 7]) == 7


def test_descending():
    # [8,7,6,5] → i=0→min(8,7)=7, i=1→max(6,5)=6 → [7,6]
    # → i=0→min(7,6)=6
    assert min_steps([8, 7, 6, 5]) == 6


def test_large_values():
    assert min_steps([1000000000, 1]) == 1


def test_sixteen_elements():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    # Round 1: min(1,2)=1, max(3,4)=4, min(5,6)=5, max(7,8)=8,
    #          min(9,10)=9, max(11,12)=12, min(13,14)=13, max(15,16)=16
    # → [1,4,5,8,9,12,13,16]
    # Round 2: min(1,4)=1, max(5,8)=8, min(9,12)=9, max(13,16)=16
    # → [1,8,9,16]
    # Round 3: min(1,8)=1, max(9,16)=16 → [1,16]
    # Round 4: min(1,16)=1
    assert min_steps(nums) == 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
