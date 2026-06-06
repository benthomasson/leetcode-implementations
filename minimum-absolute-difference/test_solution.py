from solution import minimumAbsDifference


def test_example1():
    assert minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]


def test_example2():
    assert minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]


def test_example3():
    assert minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]


def test_two_elements():
    assert minimumAbsDifference([5, 1]) == [[1, 5]]


def test_consecutive():
    assert minimumAbsDifference([5, 4, 3, 2, 1]) == [[1, 2], [2, 3], [3, 4], [4, 5]]


def test_negatives():
    assert minimumAbsDifference([-3, -7, -5]) == [[-7, -5], [-5, -3]]


def test_large_spread():
    assert minimumAbsDifference([-1000000, 0, 1000000]) == [[-1000000, 0], [0, 1000000]]


def test_single_min_pair():
    assert minimumAbsDifference([10, 20, 31]) == [[10, 20]]
