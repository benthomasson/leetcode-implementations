from solution import Solution


def test_example_1():
    """Test with first example from problem description."""
    sol = Solution()
    words = ["are", "amy", "u"]
    assert sol.vowelStrings(words, 0, 2) == 2


def test_example_2():
    """Test with second example from problem description."""
    sol = Solution()
    words = ["hey", "aeo", "mu", "ooo", "artro"]
    assert sol.vowelStrings(words, 1, 4) == 3


def test_single_element_range():
    """Test with left == right (single element)."""
    sol = Solution()
    words = ["apple", "orange", "umbrella"]
    assert sol.vowelStrings(words, 0, 0) == 1
    assert sol.vowelStrings(words, 1, 1) == 1
    assert sol.vowelStrings(words, 2, 2) == 1


def test_single_character_vowels():
    """Test with single character vowel strings."""
    sol = Solution()
    words = ["a", "e", "i", "o", "u"]
    assert sol.vowelStrings(words, 0, 4) == 5


def test_single_character_consonants():
    """Test with single character consonant strings."""
    sol = Solution()
    words = ["b", "c", "d", "f", "g"]
    assert sol.vowelStrings(words, 0, 4) == 0


def test_no_vowel_strings():
    """Test range with no vowel strings."""
    sol = Solution()
    words = ["hello", "world", "test", "python"]
    assert sol.vowelStrings(words, 0, 3) == 0


def test_all_vowel_strings():
    """Test range where all strings are vowel strings."""
    sol = Solution()
    words = ["area", "ice", "opera", "umbrella"]
    assert sol.vowelStrings(words, 0, 3) == 4


def test_mixed_cases():
    """Test mix of vowel strings and non-vowel strings."""
    sol = Solution()
    words = ["apple", "banana", "echo", "indie", "orange"]
    assert sol.vowelStrings(words, 0, 4) == 4
    assert sol.vowelStrings(words, 1, 3) == 2


def test_partial_range():
    """Test with range that doesn't cover entire array."""
    sol = Solution()
    words = ["ate", "cat", "dog", "eagle", "ink"]
    assert sol.vowelStrings(words, 2, 4) == 1


def test_larger_input():
    """Test with larger input size."""
    sol = Solution()
    words = ["a"] * 500 + ["cat"] * 500
    assert sol.vowelStrings(words, 0, 999) == 500
    assert sol.vowelStrings(words, 0, 499) == 500
    assert sol.vowelStrings(words, 500, 999) == 0
