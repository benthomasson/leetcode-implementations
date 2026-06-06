from solution import count_pairs_leftovers


def test_example_1():
    assert count_pairs_leftovers([1, 3, 2, 1, 3, 2, 2]) == [3, 1]


def test_example_2():
    assert count_pairs_leftovers([1, 1]) == [1, 0]


def test_example_3():
    assert count_pairs_leftovers([0]) == [0, 1]


def test_all_same_even():
    assert count_pairs_leftovers([2, 2, 2, 2]) == [2, 0]


def test_all_same_odd():
    assert count_pairs_leftovers([5, 5, 5]) == [1, 1]


def test_all_unique():
    assert count_pairs_leftovers([1, 2, 3]) == [0, 3]


def test_single_element():
    assert count_pairs_leftovers([100]) == [0, 1]


def test_large_count_one_number():
    assert count_pairs_leftovers([7] * 10) == [5, 0]
    assert count_pairs_leftovers([7] * 11) == [5, 1]
