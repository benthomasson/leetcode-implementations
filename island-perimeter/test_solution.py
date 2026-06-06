import unittest
from solution import Solution


class TestIslandPerimeter(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertEqual(self.s.islandPerimeter(grid), 16)

    def test_example2_single_cell(self):
        self.assertEqual(self.s.islandPerimeter([[1]]), 4)

    def test_example3_single_row(self):
        self.assertEqual(self.s.islandPerimeter([[1,0]]), 4)

    def test_single_column(self):
        self.assertEqual(self.s.islandPerimeter([[1],[1],[1]]), 8)

    def test_full_grid(self):
        grid = [[1,1],[1,1]]
        self.assertEqual(self.s.islandPerimeter(grid), 8)

    def test_l_shape(self):
        grid = [[1,0],[1,1]]
        self.assertEqual(self.s.islandPerimeter(grid), 8)

    def test_horizontal_line(self):
        grid = [[1,1,1,1]]
        self.assertEqual(self.s.islandPerimeter(grid), 10)


if __name__ == "__main__":
    unittest.main()
