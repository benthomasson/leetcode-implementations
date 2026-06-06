from solution import balanced_string


def test_example_1():
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    assert balanced_string(grid) == 8

def test_example_2():
    grid = [[3,2],[1,0]]
    assert balanced_string(grid) == 0

def test_all_negative():
    assert balanced_string([[-1,-2],[-3,-4]]) == 4

def test_all_positive():
    assert balanced_string([[5,3],[2,1]]) == 0

def test_single_negative():
    assert balanced_string([[-1]]) == 1

def test_single_positive():
    assert balanced_string([[5]]) == 0

def test_single_row():
    assert balanced_string([[3,1,-1,-2]]) == 2

def test_single_column():
    assert balanced_string([[3],[1],[-1],[-2]]) == 2

def test_zeros_boundary():
    assert balanced_string([[1,0,0],[0,0,-1],[-1,-1,-2]]) == 4
