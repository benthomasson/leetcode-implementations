from solution import countLargestGroup


def test_example1():
    assert countLargestGroup(13) == 4


def test_example2():
    assert countLargestGroup(2) == 2


def test_single():
    assert countLargestGroup(1) == 1


def test_single_digit_boundary():
    # 1-9: nine groups each of size 1
    assert countLargestGroup(9) == 9


def test_max_constraint():
    result = countLargestGroup(10000)
    assert isinstance(result, int) and result >= 1
