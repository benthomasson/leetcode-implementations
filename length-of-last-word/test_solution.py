from solution import length_of_last_word


def test_examples():
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("luffy is still joyboy") == 6


def test_trailing_spaces():
    assert length_of_last_word("Hello World   ") == 5


def test_single_word():
    assert length_of_last_word("word") == 4


def test_single_char():
    assert length_of_last_word("a") == 1


def test_leading_and_trailing_spaces():
    assert length_of_last_word("   hello   ") == 5


def test_multiple_spaces_between():
    assert length_of_last_word("a    b") == 1
