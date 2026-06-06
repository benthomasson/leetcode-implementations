import unittest
from solution import Solution


class TestHasGroupsSizeX(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))

    def test_example2(self):
        self.assertFalse(self.s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))

    def test_single_card(self):
        self.assertFalse(self.s.hasGroupsSizeX([1]))

    def test_two_same(self):
        self.assertTrue(self.s.hasGroupsSizeX([1, 1]))

    def test_all_same(self):
        self.assertTrue(self.s.hasGroupsSizeX([0, 0, 0, 0]))

    def test_coprime_counts(self):
        self.assertFalse(self.s.hasGroupsSizeX([1, 1, 1, 2, 2]))

    def test_gcd_greater_than_2(self):
        self.assertTrue(self.s.hasGroupsSizeX([1, 1, 1, 2, 2, 2]))

    def test_single_value_pair(self):
        self.assertTrue(self.s.hasGroupsSizeX([0, 0]))


if __name__ == "__main__":
    unittest.main()
