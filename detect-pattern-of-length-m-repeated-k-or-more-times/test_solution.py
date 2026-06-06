from solution import contains_pattern


def test_example_1():
    """Test pattern of length 1 repeated 4 times."""
    assert contains_pattern([1, 2, 4, 4, 4, 4], 1, 3) == True


def test_example_2():
    """Test pattern of length 2 repeated 2 times."""
    assert contains_pattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2) == True


def test_example_3():
    """Test pattern that only repeats 2 times when 3 needed."""
    assert contains_pattern([1, 2, 1, 2, 1, 3], 2, 3) == False


def test_pattern_at_beginning():
    """Test pattern at the start of array."""
    assert contains_pattern([3, 3, 3, 1, 2, 5], 1, 3) == True


def test_pattern_at_end():
    """Test pattern at the end of array."""
    assert contains_pattern([1, 2, 5, 7, 7, 7], 1, 3) == True


def test_pattern_in_middle():
    """Test pattern in the middle of array."""
    assert contains_pattern([1, 5, 5, 5, 5, 9], 1, 4) == True


def test_no_pattern_found():
    """Test when no valid pattern exists."""
    assert contains_pattern([1, 2, 3, 4, 5, 6], 2, 2) == False


def test_entire_array_is_pattern():
    """Test when entire array is a repeating pattern."""
    assert contains_pattern([1, 2, 1, 2, 1, 2], 2, 3) == True


def test_minimum_length_exact_match():
    """Test minimum array length with exact pattern match."""
    assert contains_pattern([5, 5], 1, 2) == True


def test_pattern_almost_repeats():
    """Test pattern that almost repeats but fails."""
    assert contains_pattern([1, 2, 3, 1, 2, 4], 3, 2) == False


def test_larger_pattern_multiple_repetitions():
    """Test larger pattern with multiple repetitions."""
    assert contains_pattern([1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5], 3, 3) == True


def test_single_element_pattern_exact_k():
    """Test single element pattern repeated exactly k times."""
    assert contains_pattern([7, 7, 7], 1, 3) == True


def test_pattern_longer_than_available_space():
    """Test when m * k exceeds array length."""
    assert contains_pattern([1, 2, 3], 2, 3) == False


def test_complex_pattern_with_duplicates():
    """Test complex pattern with duplicate values."""
    assert contains_pattern([1, 1, 2, 2, 1, 1, 2, 2], 4, 2) == True
