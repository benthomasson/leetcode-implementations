import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution

s = Solution()


def test_example1():
    assert s.maxValue([1, 2, 1]) == [1, 2, 1, 1, 2, 1]


def test_example2():
    assert s.maxValue([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]


def test_single_element():
    assert s.maxValue([5]) == [5, 5]


def test_all_same():
    assert s.maxValue([3, 3, 3]) == [3, 3, 3, 3, 3, 3]


def test_max_constraints():
    nums = [1000] * 1000
    result = s.maxValue(nums)
    assert len(result) == 2000
    assert all(v == 1000 for v in result)


def test_output_length():
    for n in [1, 2, 5, 10]:
        nums = list(range(1, n + 1))
        assert len(s.maxValue(nums)) == 2 * n


def test_first_half_equals_second_half():
    nums = [4, 7, 2]
    result = s.maxValue(nums)
    assert result[:len(nums)] == result[len(nums):]
