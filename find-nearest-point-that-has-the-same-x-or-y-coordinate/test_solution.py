from solution import nearestValidPoint


def test_example_1():
    assert nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]) == 2

def test_example_2():
    assert nearestValidPoint(3, 4, [[3,4]]) == 0

def test_example_3():
    assert nearestValidPoint(3, 4, [[2,3]]) == -1

def test_all_valid():
    assert nearestValidPoint(2, 2, [[2,1],[2,3],[1,2],[3,2]]) == 0

def test_no_valid():
    assert nearestValidPoint(1, 1, [[2,2],[3,3]]) == -1

def test_tie_smallest_index():
    # Both [1,4] and [5,4] have distance 2, pick index 0
    assert nearestValidPoint(3, 4, [[1,4],[5,4]]) == 0

def test_same_location():
    assert nearestValidPoint(5, 5, [[5,5]]) == 0

def test_single_valid():
    assert nearestValidPoint(1, 1, [[2,2],[1,5]]) == 1

def test_boundary_values():
    assert nearestValidPoint(10000, 10000, [[10000,1],[1,10000]]) == 0
