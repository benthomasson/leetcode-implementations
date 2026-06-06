import unittest
from solution import Solution


class TestNumberOfSubstrings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.numberOfSubstrings([1, 2, 3, 4], [2, 4, 1, 3]))

    def test_example2(self):
        self.assertTrue(self.s.numberOfSubstrings([7], [7]))

    def test_example3(self):
        self.assertFalse(self.s.numberOfSubstrings([3, 7, 9], [3, 7, 11]))

    def test_already_equal(self):
        self.assertTrue(self.s.numberOfSubstrings([1, 2, 3], [1, 2, 3]))

    def test_all_same(self):
        self.assertTrue(self.s.numberOfSubstrings([5, 5, 5], [5, 5, 5]))

    def test_duplicates_different_freq(self):
        self.assertFalse(self.s.numberOfSubstrings([1, 1, 2], [1, 2, 2]))

    def test_single_different(self):
        self.assertFalse(self.s.numberOfSubstrings([1], [2]))

    def test_reversed(self):
        self.assertTrue(self.s.numberOfSubstrings([1, 2, 3], [3, 2, 1]))


if __name__ == "__main__":
    unittest.main()
