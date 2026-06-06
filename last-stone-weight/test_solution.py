import unittest
from solution import Solution


class TestLastStoneWeight(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)

    def test_single_stone(self):
        self.assertEqual(self.s.lastStoneWeight([1]), 1)

    def test_two_equal(self):
        self.assertEqual(self.s.lastStoneWeight([3, 3]), 0)

    def test_two_unequal(self):
        self.assertEqual(self.s.lastStoneWeight([5, 2]), 3)

    def test_all_equal(self):
        self.assertEqual(self.s.lastStoneWeight([4, 4, 4, 4]), 0)

    def test_all_equal_odd_count(self):
        self.assertEqual(self.s.lastStoneWeight([4, 4, 4]), 4)

    def test_descending(self):
        self.assertEqual(self.s.lastStoneWeight([10, 5, 3, 1]), 1)

    def test_max_weight(self):
        self.assertEqual(self.s.lastStoneWeight([1000, 1000]), 0)


if __name__ == "__main__":
    unittest.main()
