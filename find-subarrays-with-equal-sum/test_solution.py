from solution import equal_sum_subarrays


def test_example1():
    assert equal_sum_subarrays([4, 2, 4]) is True

def test_example2():
    assert equal_sum_subarrays([1, 2, 3, 4, 5]) is False

def test_example3():
    assert equal_sum_subarrays([0, 0, 0]) is True

def test_min_length_no_match():
    assert equal_sum_subarrays([1, 2]) is False

def test_negative_numbers():
    assert equal_sum_subarrays([-1, 2, -1, 2]) is True

def test_all_same():
    assert equal_sum_subarrays([5, 5, 5, 5]) is True

def test_large_values():
    assert equal_sum_subarrays([10**9, -(10**9), 10**9, -(10**9)]) is True

def test_two_elements_same():
    assert equal_sum_subarrays([3, 3]) is False
