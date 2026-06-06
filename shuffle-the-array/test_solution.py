import unittest
from solution import Solution


class TestShuffle(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.shuffle([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])

    def test_example2(self):
        self.assertEqual(self.s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4), [1, 4, 2, 3, 3, 2, 4, 1])

    def test_example3(self):
        self.assertEqual(self.s.shuffle([1, 1, 2, 2], 2), [1, 2, 1, 2])

    def test_n1(self):
        self.assertEqual(self.s.shuffle([1, 2], 1), [1, 2])

    def test_all_same(self):
        self.assertEqual(self.s.shuffle([5, 5, 5, 5], 2), [5, 5, 5, 5])

    def test_max_n(self):
        nums = list(range(1, 1001))
        result = self.s.shuffle(nums, 500)
        self.assertEqual(len(result), 1000)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 501)


if __name__ == "__main__":
    unittest.main()
