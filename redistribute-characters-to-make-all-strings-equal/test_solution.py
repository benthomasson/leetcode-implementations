from solution import redistribute_characters_to_make_all_strings_equal


def test_example_1():
    assert redistribute_characters_to_make_all_strings_equal(["abc", "aabc", "bc"]) is True


def test_example_2():
    assert redistribute_characters_to_make_all_strings_equal(["ab", "a"]) is False


def test_single_word():
    assert redistribute_characters_to_make_all_strings_equal(["abc"]) is True


def test_identical_words():
    assert redistribute_characters_to_make_all_strings_equal(["aa", "aa", "aa"]) is True


def test_all_same_char_uneven():
    assert redistribute_characters_to_make_all_strings_equal(["a", "aa"]) is False


def test_all_same_char_even():
    assert redistribute_characters_to_make_all_strings_equal(["aa", "a", "a", "aa"]) is False


def test_many_distinct_chars():
    assert redistribute_characters_to_make_all_strings_equal(["ab", "cd", "ef"]) is False


def test_two_empty_style():
    # All chars divisible by 2
    assert redistribute_characters_to_make_all_strings_equal(["aabb", "bbaa"]) is True


def test_single_char_strings():
    assert redistribute_characters_to_make_all_strings_equal(["a", "b", "c"]) is False
