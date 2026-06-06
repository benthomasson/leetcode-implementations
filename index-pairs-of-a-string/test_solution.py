import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution, has_all_codes_in_range
import unittest


class TestIndexPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        assert self.sol.indexPairs("thestoryofleetcodeandme", ["story", "fleet", "leetcode"]) == [[3, 7], [9, 13], [10, 17]]

    def test_example2(self):
        assert self.sol.indexPairs("ababa", ["aba", "ab"]) == [[0, 1], [0, 2], [2, 3], [2, 4]]

    def test_no_match(self):
        assert self.sol.indexPairs("hello", ["xyz"]) == []

    def test_single_char_match(self):
        assert self.sol.indexPairs("a", ["a"]) == [[0, 0]]

    def test_full_string_match(self):
        assert self.sol.indexPairs("abc", ["abc"]) == [[0, 2]]

    def test_word_longer_than_text(self):
        assert self.sol.indexPairs("ab", ["abcd"]) == []

    def test_multiple_occurrences_same_word(self):
        assert self.sol.indexPairs("aaa", ["a"]) == [[0, 0], [1, 1], [2, 2]]

    def test_wrapper_function(self):
        assert has_all_codes_in_range("ababa", ["aba", "ab"]) == [[0, 1], [0, 2], [2, 3], [2, 4]]


if __name__ == '__main__':
    unittest.main()
