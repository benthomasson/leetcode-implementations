import unittest
from solution import Solution


class TestMinStartValue(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxSideLength([-3, 2, -3, 4, 2]), 5)

    def test_example2(self):
        self.assertEqual(self.s.maxSideLength([1, 2]), 1)

    def test_example3(self):
        self.assertEqual(self.s.maxSideLength([1, -2, -3]), 5)

    def test_all_positive(self):
        self.assertEqual(self.s.maxSideLength([3, 5, 2]), 1)

    def test_all_negative(self):
        self.assertEqual(self.s.maxSideLength([-1, -2, -3]), 7)

    def test_single_positive(self):
        self.assertEqual(self.s.maxSideLength([5]), 1)

    def test_single_negative(self):
        self.assertEqual(self.s.maxSideLength([-5]), 6)

    def test_zeros(self):
        self.assertEqual(self.s.maxSideLength([0, 0, 0]), 1)


if __name__ == "__main__":
    unittest.main()
