import unittest
from solution import Solution


class TestDivideArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_true(self):
        self.assertTrue(self.s.divideArray([3, 2, 3, 2, 2, 2]))

    def test_example2_false(self):
        self.assertFalse(self.s.divideArray([1, 2, 3, 4]))

    def test_single_pair(self):
        self.assertTrue(self.s.divideArray([1, 1]))

    def test_single_pair_false(self):
        self.assertFalse(self.s.divideArray([1, 2]))

    def test_all_same(self):
        self.assertTrue(self.s.divideArray([5, 5, 5, 5]))

    def test_odd_count(self):
        self.assertFalse(self.s.divideArray([1, 1, 1, 2]))

    def test_multiple_pairs(self):
        self.assertTrue(self.s.divideArray([1, 1, 2, 2, 3, 3]))

    def test_four_of_a_kind(self):
        self.assertTrue(self.s.divideArray([7, 7, 7, 7]))

    def test_mixed_odd_counts(self):
        self.assertFalse(self.s.divideArray([1, 1, 1, 2, 2, 2]))


if __name__ == "__main__":
    unittest.main()
