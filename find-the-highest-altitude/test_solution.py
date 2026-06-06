from solution import min_operations


def test_example_1():
    assert min_operations([-5, 1, 5, 0, -7]) == 1


def test_example_2():
    assert min_operations([-4, -3, -2, -1, 4, 3, 2]) == 0


def test_single_positive():
    assert min_operations([5]) == 5


def test_single_negative():
    assert min_operations([-3]) == 0


def test_all_positive():
    assert min_operations([1, 2, 3]) == 6


def test_all_negative():
    assert min_operations([-1, -2, -3]) == 0


def test_all_zeros():
    assert min_operations([0, 0, 0]) == 0


def test_peak_in_middle():
    assert min_operations([3, 2, -4, -1]) == 5
