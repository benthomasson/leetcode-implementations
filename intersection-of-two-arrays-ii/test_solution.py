from solution import intersect


def test_example1():
    assert sorted(intersect([1, 2, 2, 1], [2, 2])) == [2, 2]


def test_example2():
    assert sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]


def test_no_overlap():
    assert intersect([1, 2], [3, 4]) == []


def test_identical():
    assert sorted(intersect([1, 2, 3], [1, 2, 3])) == [1, 2, 3]


def test_single_element_match():
    assert intersect([1], [1]) == [1]


def test_single_element_no_match():
    assert intersect([1], [2]) == []


def test_all_duplicates():
    assert sorted(intersect([2, 2, 2], [2, 2])) == [2, 2]


def test_subset():
    assert sorted(intersect([1, 2], [1, 2, 3, 4])) == [1, 2]
