from solution import maxNumberOfCandies


def test_example1():
    assert maxNumberOfCandies([1, 1, 2, 2, 3, 3]) == 3


def test_example2():
    assert maxNumberOfCandies([1, 1, 2, 3]) == 2


def test_example3():
    assert maxNumberOfCandies([6, 6, 6, 6]) == 1


def test_all_different():
    assert maxNumberOfCandies([1, 2, 3, 4]) == 2


def test_min_length():
    assert maxNumberOfCandies([1, 1]) == 1
    assert maxNumberOfCandies([1, 2]) == 1


def test_negative_types():
    assert maxNumberOfCandies([-1, -1, -2, -2]) == 2


def test_mixed_sign_types():
    assert maxNumberOfCandies([-1, 0, 1, 2]) == 2


def test_large_single_type():
    assert maxNumberOfCandies([5] * 100) == 1


def test_many_unique_types():
    assert maxNumberOfCandies(list(range(100))) == 50
