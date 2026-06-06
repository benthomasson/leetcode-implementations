import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution

import unittest


class TestNumTilePossibilities(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.num_tile_possibilities(["cat", "bt", "hat", "tree"], "atach"), 6)

    def test_example2(self):
        self.assertEqual(self.sol.num_tile_possibilities(["hello", "world", "leetcode"], "welldonehoneyr"), 10)

    def test_empty_words(self):
        self.assertEqual(self.sol.num_tile_possibilities([], "abc"), 0)

    def test_no_good_words(self):
        self.assertEqual(self.sol.num_tile_possibilities(["xyz", "pqr"], "abc"), 0)

    def test_all_good_words(self):
        self.assertEqual(self.sol.num_tile_possibilities(["a", "b", "ab"], "abc"), 4)

    def test_word_needs_duplicate_char(self):
        self.assertEqual(self.sol.num_tile_possibilities(["aab"], "ab"), 0)
        self.assertEqual(self.sol.num_tile_possibilities(["aab"], "aab"), 3)

    def test_single_char(self):
        self.assertEqual(self.sol.num_tile_possibilities(["a"], "a"), 1)
        self.assertEqual(self.sol.num_tile_possibilities(["b"], "a"), 0)

    def test_duplicate_words_counted_independently(self):
        self.assertEqual(self.sol.num_tile_possibilities(["a", "a"], "ab"), 2)


if __name__ == "__main__":
    unittest.main()
