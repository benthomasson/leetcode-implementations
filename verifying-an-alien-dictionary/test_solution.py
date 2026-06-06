import unittest
from solution import reverse_string


class TestReverseString(unittest.TestCase):

    def test_example1_sorted(self):
        assert reverse_string(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") is True

    def test_example2_unsorted(self):
        assert reverse_string(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") is False

    def test_example3_prefix(self):
        assert reverse_string(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") is False

    def test_single_word(self):
        assert reverse_string(["only"], "abcdefghijklmnopqrstuvwxyz") is True

    def test_identical_words(self):
        assert reverse_string(["abc", "abc"], "abcdefghijklmnopqrstuvwxyz") is True

    def test_prefix_shorter_first(self):
        assert reverse_string(["app", "apple"], "abcdefghijklmnopqrstuvwxyz") is True

    def test_reversed_order(self):
        assert reverse_string(["ba", "ab"], "zyxwvutsrqponmlkjihgfedcba") is True

    def test_all_same_single_char(self):
        assert reverse_string(["a", "a", "a"], "abcdefghijklmnopqrstuvwxyz") is True

    def test_differ_at_second_char(self):
        assert reverse_string(["ab", "ac"], "abcdefghijklmnopqrstuvwxyz") is True
        assert reverse_string(["ac", "ab"], "abcdefghijklmnopqrstuvwxyz") is False


if __name__ == "__main__":
    unittest.main()
