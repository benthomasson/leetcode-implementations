from solution import duplicateZeros


def test_example1():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicateZeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]


def test_example2():
    arr = [1, 2, 3]
    duplicateZeros(arr)
    assert arr == [1, 2, 3]


def test_all_zeros():
    arr = [0, 0, 0]
    duplicateZeros(arr)
    assert arr == [0, 0, 0]


def test_no_zeros():
    arr = [1, 2, 3, 4]
    duplicateZeros(arr)
    assert arr == [1, 2, 3, 4]


def test_single_zero():
    arr = [0]
    duplicateZeros(arr)
    assert arr == [0]


def test_single_nonzero():
    arr = [5]
    duplicateZeros(arr)
    assert arr == [5]


def test_zero_at_end():
    arr = [1, 2, 0]
    duplicateZeros(arr)
    assert arr == [1, 2, 0]


def test_boundary_zero():
    """Zero at boundary where only one copy fits."""
    arr = [8, 4, 5, 0, 0, 0, 0, 7]
    duplicateZeros(arr)
    assert arr == [8, 4, 5, 0, 0, 0, 0, 0]
