import unittest
from solution import Solution


class TestIsBoomerang(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_true(self):
        self.assertTrue(self.s.isBoomerang([[1, 1], [2, 3], [3, 2]]))

    def test_collinear(self):
        self.assertFalse(self.s.isBoomerang([[1, 1], [2, 2], [3, 3]]))

    def test_duplicate_points(self):
        self.assertFalse(self.s.isBoomerang([[1, 1], [1, 1], [2, 3]]))

    def test_all_same(self):
        self.assertFalse(self.s.isBoomerang([[0, 0], [0, 0], [0, 0]]))

    def test_horizontal_line(self):
        self.assertFalse(self.s.isBoomerang([[0, 0], [1, 0], [2, 0]]))

    def test_vertical_line(self):
        self.assertFalse(self.s.isBoomerang([[0, 0], [0, 1], [0, 2]]))

    def test_boundary_collinear(self):
        self.assertFalse(self.s.isBoomerang([[0, 0], [50, 50], [100, 100]]))

    def test_boundary_boomerang(self):
        self.assertTrue(self.s.isBoomerang([[0, 0], [50, 51], [100, 100]]))


if __name__ == "__main__":
    unittest.main()
