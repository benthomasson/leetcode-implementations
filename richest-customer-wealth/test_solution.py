import unittest
from solution import Solution


class TestMaximumWealth(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)

    def test_example2(self):
        self.assertEqual(self.s.maximumWealth([[1, 5], [7, 3], [3, 5]]), 10)

    def test_example3(self):
        self.assertEqual(self.s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)

    def test_single_customer(self):
        self.assertEqual(self.s.maximumWealth([[4, 5, 6]]), 15)

    def test_single_bank(self):
        self.assertEqual(self.s.maximumWealth([[3], [7], [2]]), 7)

    def test_1x1(self):
        self.assertEqual(self.s.maximumWealth([[42]]), 42)

    def test_all_equal(self):
        self.assertEqual(self.s.maximumWealth([[5, 5], [5, 5], [5, 5]]), 10)

    def test_max_constraints(self):
        accounts = [[100] * 50 for _ in range(50)]
        self.assertEqual(self.s.maximumWealth(accounts), 5000)


if __name__ == "__main__":
    unittest.main()
