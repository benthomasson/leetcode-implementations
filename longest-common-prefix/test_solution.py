"""Tests for longest_common_prefix."""

import unittest
from solution import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):

    def test_example1(self):
        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    def test_example2(self):
        assert longest_common_prefix(["dog", "racecar", "car"]) == ""

    def test_single_string(self):
        assert longest_common_prefix(["alone"]) == "alone"

    def test_empty_list(self):
        assert longest_common_prefix([]) == ""

    def test_all_identical(self):
        assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"

    def test_no_common_prefix(self):
        assert longest_common_prefix(["a", "b", "c"]) == ""

    def test_single_char_strings(self):
        assert longest_common_prefix(["a", "a", "a"]) == "a"

    def test_empty_string_in_list(self):
        assert longest_common_prefix(["", "abc", "abd"]) == ""

    def test_all_empty_strings(self):
        assert longest_common_prefix(["", "", ""]) == ""

    def test_full_prefix_match(self):
        assert longest_common_prefix(["ab", "abc", "abcd"]) == "ab"


if __name__ == "__main__":
    unittest.main()
