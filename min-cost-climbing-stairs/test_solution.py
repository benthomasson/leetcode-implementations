import unittest
from solution import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minCostClimbingStairs([10, 15, 20]), 15)

    def test_example2(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_two_elements(self):
        self.assertEqual(self.s.minCostClimbingStairs([5, 10]), 5)

    def test_all_zeros(self):
        self.assertEqual(self.s.minCostClimbingStairs([0, 0, 0, 0]), 0)

    def test_all_same(self):
        self.assertEqual(self.s.minCostClimbingStairs([3, 3, 3]), 3)

    def test_ascending(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 2, 3, 4, 5]), 6)

    def test_descending(self):
        self.assertEqual(self.s.minCostClimbingStairs([5, 4, 3, 2, 1]), 6)


if __name__ == "__main__":
    unittest.main()
