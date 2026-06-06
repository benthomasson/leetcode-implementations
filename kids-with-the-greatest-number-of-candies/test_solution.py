import unittest
from solution import Solution


class TestKidsWithCandies(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.kidsWithCandies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])

    def test_example2(self):
        self.assertEqual(self.s.kidsWithCandies([4, 2, 1, 1, 2], 1), [True, False, False, False, False])

    def test_example3(self):
        self.assertEqual(self.s.kidsWithCandies([12, 1, 12], 10), [True, False, True])

    def test_all_equal(self):
        self.assertEqual(self.s.kidsWithCandies([5, 5, 5], 1), [True, True, True])

    def test_minimum_n(self):
        self.assertEqual(self.s.kidsWithCandies([1, 2], 1), [True, True])

    def test_large_extra_all_qualify(self):
        self.assertEqual(self.s.kidsWithCandies([1, 100, 1], 50), [False, True, False])

    def test_extra_makes_everyone_greatest(self):
        self.assertEqual(self.s.kidsWithCandies([1, 2, 3], 50), [True, True, True])


if __name__ == "__main__":
    unittest.main()
