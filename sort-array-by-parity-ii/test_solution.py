import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution


def check_parity(nums):
    """Verify every even index has even value and every odd index has odd value."""
    return all(nums[i] % 2 == i % 2 for i in range(len(nums)))


def test_example1():
    s = Solution()
    nums = [4, 2, 5, 7]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == [2, 4, 5, 7]


def test_example2():
    s = Solution()
    nums = [2, 3]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == [2, 3]


def test_already_sorted():
    s = Solution()
    nums = [0, 1, 2, 3]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == [0, 1, 2, 3]


def test_reversed_parity():
    s = Solution()
    nums = [1, 2, 3, 4]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == [1, 2, 3, 4]


def test_with_zeros():
    s = Solution()
    nums = [0, 1, 0, 3]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == [0, 0, 1, 3]


def test_larger():
    s = Solution()
    nums = [4, 2, 5, 7, 6, 8, 1, 3]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == sorted([4, 2, 5, 7, 6, 8, 1, 3])


def test_in_place():
    s = Solution()
    nums = [4, 2, 5, 7]
    result = s.possible_bipartition(nums)
    assert result is nums, "Should modify in-place and return same list"


def test_all_same_even_odd():
    """All evens are same value, all odds are same value."""
    s = Solution()
    nums = [2, 1, 2, 1, 2, 1]
    result = s.possible_bipartition(nums)
    assert check_parity(result)
    assert sorted(result) == [1, 1, 1, 2, 2, 2]


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
