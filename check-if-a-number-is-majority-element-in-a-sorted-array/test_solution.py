import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import is_majority_element


def test_example1_majority():
    assert is_majority_element([2, 4, 5, 5, 5, 5, 5, 6, 6], 5) is True

def test_example2_not_majority():
    assert is_majority_element([10, 100, 101, 101], 101) is False

def test_single_element_match():
    assert is_majority_element([7], 7) is True

def test_single_element_no_match():
    assert is_majority_element([7], 3) is False

def test_exactly_half_not_majority():
    assert is_majority_element([1, 1, 2, 2], 1) is False

def test_all_same():
    assert is_majority_element([5, 5, 5], 5) is True

def test_target_absent():
    assert is_majority_element([1, 2, 3, 4, 5], 6) is False

def test_target_at_end_not_majority():
    assert is_majority_element([1, 2, 3, 3], 3) is False

def test_just_over_half():
    # 3 appears 3 times in length-5 array: 3 > 2.5 → True
    assert is_majority_element([1, 3, 3, 3, 5], 3) is True

def test_two_elements_majority():
    assert is_majority_element([1, 1, 1, 2], 1) is True


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
