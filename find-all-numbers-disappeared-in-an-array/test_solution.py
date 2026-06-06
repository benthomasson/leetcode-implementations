from solution import find_disappeared_numbers


def test_example1():
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


def test_example2():
    assert find_disappeared_numbers([1, 1]) == [2]


def test_no_missing():
    assert find_disappeared_numbers([1, 2, 3]) == []


def test_single_present():
    assert find_disappeared_numbers([1]) == []


def test_single_missing():
    assert find_disappeared_numbers([2, 2]) == [1]


def test_all_same():
    assert find_disappeared_numbers([1, 1, 1, 1]) == [2, 3, 4]


def test_reverse_order():
    assert find_disappeared_numbers([3, 2, 1]) == []


def test_large():
    n = 100000
    nums = list(range(1, n + 1))
    nums[0] = 2  # replace 1 with duplicate 2
    nums[-1] = 2  # replace n with duplicate 2
    result = find_disappeared_numbers(nums)
    assert result == [1, n]
