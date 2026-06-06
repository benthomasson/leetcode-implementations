from solution import count_elements


def test_example1():
    assert count_elements([1, 2, 3]) == 2

def test_example2():
    assert count_elements([1, 1, 3, 3, 5, 5, 7, 7]) == 0

def test_duplicates_with_successor():
    assert count_elements([1, 1, 2, 2]) == 2

def test_single_element():
    assert count_elements([5]) == 0

def test_empty():
    assert count_elements([]) == 0

def test_consecutive_run():
    assert count_elements([1, 2, 3, 4, 5]) == 4

def test_boundary_values():
    assert count_elements([0, 1, 999, 1000]) == 2

def test_all_identical():
    assert count_elements([3, 3, 3]) == 0
