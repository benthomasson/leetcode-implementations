import unittest
from solution import Solution


class TestLargeGroupPositions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.largeGroupPositions("abbxxxxzzy"), [[3, 6]])

    def test_example2(self):
        self.assertEqual(self.sol.largeGroupPositions("abc"), [])

    def test_example3(self):
        self.assertEqual(self.sol.largeGroupPositions("abcdddeeeeaabbbcd"), [[3, 5], [6, 9], [12, 14]])

    def test_single_char(self):
        self.assertEqual(self.sol.largeGroupPositions("a"), [])

    def test_all_same_large(self):
        self.assertEqual(self.sol.largeGroupPositions("aaaa"), [[0, 3]])

    def test_exactly_three(self):
        self.assertEqual(self.sol.largeGroupPositions("aaa"), [[0, 2]])

    def test_exactly_two(self):
        self.assertEqual(self.sol.largeGroupPositions("aa"), [])

    def test_large_group_at_end(self):
        self.assertEqual(self.sol.largeGroupPositions("abccc"), [[2, 4]])

    def test_multiple_adjacent_large(self):
        self.assertEqual(self.sol.largeGroupPositions("aaabbb"), [[0, 2], [3, 5]])

    def test_all_same_char_long(self):
        self.assertEqual(self.sol.largeGroupPositions("zzzzzz"), [[0, 5]])


if __name__ == "__main__":
    unittest.main()
