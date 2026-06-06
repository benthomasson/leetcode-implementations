from solution import fixedPoint


def test_example1():
    assert fixedPoint([-10, -5, 0, 3, 7]) == 3

def test_example2():
    assert fixedPoint([0, 2, 5, 8, 17]) == 0

def test_example3():
    assert fixedPoint([-10, -5, 3, 4, 7, 9]) == -1

def test_single_match():
    assert fixedPoint([0]) == 0

def test_single_no_match():
    assert fixedPoint([1]) == -1

def test_fixed_point_at_end():
    assert fixedPoint([-5, -3, -1, 3]) == 3

def test_all_negative():
    assert fixedPoint([-3, -2, -1]) == -1

def test_all_too_high():
    assert fixedPoint([5, 6, 7]) == -1

def test_multiple_fixed_points_returns_smallest():
    # arr[1]==1 and arr[3]==3 and arr[4]==4; should return 1
    assert fixedPoint([-1, 1, 2, 3, 4]) == 1

def test_large_array():
    arr = list(range(1000))  # every index is a fixed point
    assert fixedPoint(arr) == 0
