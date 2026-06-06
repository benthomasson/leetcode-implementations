import unittest
from solution import Solution


class TestTranspose(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_square(self):
        self.assertEqual(self.s.transpose([[1,2,3],[4,5,6],[7,8,9]]),
                         [[1,4,7],[2,5,8],[3,6,9]])

    def test_rectangular(self):
        self.assertEqual(self.s.transpose([[1,2,3],[4,5,6]]),
                         [[1,4],[2,5],[3,6]])

    def test_single_row(self):
        self.assertEqual(self.s.transpose([[1,2,3]]), [[1],[2],[3]])

    def test_single_column(self):
        self.assertEqual(self.s.transpose([[1],[2],[3]]), [[1,2,3]])

    def test_1x1(self):
        self.assertEqual(self.s.transpose([[5]]), [[5]])

    def test_negative_values(self):
        self.assertEqual(self.s.transpose([[-1,2],[-3,4]]),
                         [[-1,-3],[2,4]])


if __name__ == "__main__":
    unittest.main()
