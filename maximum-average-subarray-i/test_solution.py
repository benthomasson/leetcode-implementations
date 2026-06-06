import unittest
from solution import Solution


class TestFindMaxAverage(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertAlmostEqual(self.s.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)

    def test_example2(self):
        self.assertAlmostEqual(self.s.findMaxAverage([5], 1), 5.0)

    def test_all_negative(self):
        self.assertAlmostEqual(self.s.findMaxAverage([-1, -2, -3, -4], 2), -1.5)

    def test_all_same(self):
        self.assertAlmostEqual(self.s.findMaxAverage([7, 7, 7, 7], 3), 7.0)

    def test_k_equals_length(self):
        self.assertAlmostEqual(self.s.findMaxAverage([1, 2, 3], 3), 2.0)

    def test_max_at_end(self):
        self.assertAlmostEqual(self.s.findMaxAverage([0, 0, 0, 10], 1), 10.0)


if __name__ == "__main__":
    unittest.main()
