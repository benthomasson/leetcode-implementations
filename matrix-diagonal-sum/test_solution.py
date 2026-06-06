import unittest
from solution import Solution


class TestDiagonalSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_3x3(self):
        self.assertEqual(self.s.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]), 25)

    def test_4x4(self):
        self.assertEqual(self.s.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]), 8)

    def test_1x1(self):
        self.assertEqual(self.s.diagonalSum([[5]]), 5)

    def test_2x2(self):
        self.assertEqual(self.s.diagonalSum([[1,2],[3,4]]), 10)

    def test_5x5(self):
        mat = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
        # Primary: 1+7+13+19+25=65, Secondary: 5+9+13+17+21=65, center 13 counted once
        self.assertEqual(self.s.diagonalSum(mat), 65 + 65 - 13)


if __name__ == "__main__":
    unittest.main()
