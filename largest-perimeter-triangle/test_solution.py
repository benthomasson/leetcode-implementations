from solution import largest_perimeter_triangle


def test_basic_valid():
    assert largest_perimeter_triangle([2, 1, 2]) == 5


def test_no_valid_triangle():
    assert largest_perimeter_triangle([1, 2, 1, 10]) == 0


def test_all_equal():
    assert largest_perimeter_triangle([3, 3, 3]) == 9


def test_minimum_length():
    assert largest_perimeter_triangle([1, 1, 1]) == 3


def test_degenerate_not_valid():
    # a + b == c is not valid (zero area)
    assert largest_perimeter_triangle([1, 2, 3]) == 0


def test_large_values():
    assert largest_perimeter_triangle([1000000, 1000000, 1000000]) == 3000000


def test_later_triplet_valid():
    assert largest_perimeter_triangle([10, 1, 2, 2]) == 5


def test_sorted_ascending():
    assert largest_perimeter_triangle([3, 4, 5]) == 12
