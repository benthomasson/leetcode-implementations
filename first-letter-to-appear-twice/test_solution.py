from solution import first_letter_to_appear_twice


def test_example1():
    assert first_letter_to_appear_twice("abccbaacz") == "c"


def test_example2():
    assert first_letter_to_appear_twice("abcdd") == "d"


def test_adjacent_duplicate():
    assert first_letter_to_appear_twice("aa") == "a"


def test_duplicate_at_end():
    assert first_letter_to_appear_twice("abcdefga") == "a"


def test_all_same():
    assert first_letter_to_appear_twice("zzzzz") == "z"


def test_multiple_duplicates_first_wins():
    assert first_letter_to_appear_twice("abcabc") == "a"
