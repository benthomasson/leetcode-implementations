from solution import sum_zero


def test_example1():
    assert sum_zero([1, 2, 3]) == 2

def test_example2():
    assert sum_zero([1, 1, 3, 3, 5, 5, 7, 7]) == 0

def test_duplicates_with_successor():
    assert sum_zero([1, 1, 2, 2]) == 2

def test_single_element():
    assert sum_zero([5]) == 0

def test_empty():
    assert sum_zero([]) == 0

def test_consecutive_run():
    assert sum_zero([1, 2, 3, 4, 5]) == 4

def test_boundary_values():
    assert sum_zero([0, 1, 999, 1000]) == 2

def test_all_identical():
    assert sum_zero([3, 3, 3]) == 0
