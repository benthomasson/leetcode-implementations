from solution import min_area_rect


def test_basic_valid():
    assert min_area_rect([2, 1, 2]) == 5


def test_no_valid_triangle():
    assert min_area_rect([1, 2, 1, 10]) == 0


def test_all_equal():
    assert min_area_rect([3, 3, 3]) == 9


def test_minimum_length():
    assert min_area_rect([1, 1, 1]) == 3


def test_degenerate_not_valid():
    # a + b == c is not valid (zero area)
    assert min_area_rect([1, 2, 3]) == 0


def test_large_values():
    assert min_area_rect([1000000, 1000000, 1000000]) == 3000000


def test_later_triplet_valid():
    assert min_area_rect([10, 1, 2, 2]) == 5


def test_sorted_ascending():
    assert min_area_rect([3, 4, 5]) == 12
