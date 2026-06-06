from solution import firstUniqChar


def test_examples():
    assert firstUniqChar("leetcode") == 0
    assert firstUniqChar("loveleetcode") == 2
    assert firstUniqChar("aabb") == -1


def test_single_char():
    assert firstUniqChar("a") == 0


def test_all_duplicates():
    assert firstUniqChar("aabbcc") == -1


def test_all_unique():
    assert firstUniqChar("abcdef") == 0


def test_last_char_unique():
    assert firstUniqChar("aabbccd") == 6


def test_repeated_pattern():
    # "abacabad": a:4, b:2, c:1, d:1 -> first unique is c at index 3
    assert firstUniqChar("abacabad") == 3
