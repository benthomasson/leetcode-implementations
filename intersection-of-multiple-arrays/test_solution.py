from solution import intersection


def test_example1():
    assert intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]) == [3, 4]


def test_example2():
    assert intersection([[1, 2, 3], [4, 5, 6]]) == []


def test_single_array():
    assert intersection([[5, 3, 1]]) == [1, 3, 5]


def test_identical_arrays():
    assert intersection([[1, 2], [1, 2], [1, 2]]) == [1, 2]


def test_single_element_arrays():
    assert intersection([[1], [1], [1]]) == [1]


def test_single_element_no_overlap():
    assert intersection([[1], [2]]) == []


def test_boundary_values():
    assert intersection([[1, 1000], [1, 1000]]) == [1, 1000]
