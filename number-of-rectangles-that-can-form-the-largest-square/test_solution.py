import unittest
from solution import Solution


class TestNumberOfSets(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.numberOfSets([[5, 8], [3, 9], [5, 12], [16, 5]]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.numberOfSets([[2, 3], [3, 7], [4, 3], [3, 7]]), 3)

    def test_single_rectangle(self):
        self.assertEqual(self.sol.numberOfSets([[3, 5]]), 1)

    def test_all_same_max_side(self):
        self.assertEqual(self.sol.numberOfSets([[4, 7], [6, 4], [4, 9]]), 3)

    def test_large_values(self):
        self.assertEqual(self.sol.numberOfSets([[999999999, 1000000000], [1000000000, 999999999]]), 2)

    def test_different_max_sides(self):
        self.assertEqual(self.sol.numberOfSets([[2, 3], [5, 10]]), 1)

    def test_descending_order(self):
        self.assertEqual(self.sol.numberOfSets([[10, 20], [5, 8], [3, 4]]), 1)


if __name__ == "__main__":
    unittest.main()
