import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import findLHS


def test_example1():
    assert findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5

def test_example2():
    assert findLHS([1, 2, 3, 4]) == 2

def test_example3_all_same():
    assert findLHS([1, 1, 1, 1]) == 0

def test_single_element():
    assert findLHS([42]) == 0

def test_two_consecutive():
    assert findLHS([1, 2]) == 2

def test_two_non_consecutive():
    assert findLHS([1, 3]) == 0

def test_negatives():
    assert findLHS([-3, -2, -2, -3, -3]) == 5

def test_large_values():
    assert findLHS([10**9, 10**9 - 1, 10**9 - 1]) == 3

def test_many_duplicates():
    assert findLHS([5, 5, 5, 6, 6, 6, 6]) == 7
