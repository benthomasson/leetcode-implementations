from solution import can_construct


def test_example_1():
    assert can_construct("a", "b") is False

def test_example_2():
    assert can_construct("aa", "ab") is False

def test_example_3():
    assert can_construct("aa", "aab") is True

def test_empty_ransom_note():
    assert can_construct("", "anything") is True

def test_single_char_match():
    assert can_construct("a", "a") is True

def test_single_char_no_match():
    assert can_construct("a", "b") is False

def test_exact_match():
    assert can_construct("abc", "abc") is True

def test_magazine_shorter():
    assert can_construct("abc", "ab") is False

def test_all_same_characters():
    assert can_construct("aaa", "aaaa") is True

def test_all_same_insufficient():
    assert can_construct("aaaa", "aaa") is False

def test_duplicate_letters_needed():
    assert can_construct("aabb", "aabbc") is True

def test_long_strings():
    assert can_construct("a" * 100000, "a" * 100000) is True
