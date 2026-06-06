import unittest
from solution import Solution


class TestFindTheDistanceValue(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2), 2)

    def test_example2(self):
        self.assertEqual(self.s.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3), 2)

    def test_example3(self):
        self.assertEqual(self.s.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6), 1)

    def test_d_zero(self):
        self.assertEqual(self.s.findTheDistanceValue([1, 2, 3], [1, 2, 3], 0), 0)

    def test_all_qualify(self):
        self.assertEqual(self.s.findTheDistanceValue([1, 2, 3], [100, 200], 5), 3)

    def test_none_qualify(self):
        self.assertEqual(self.s.findTheDistanceValue([1, 2, 3], [1, 2, 3], 100), 0)

    def test_single_elements(self):
        self.assertEqual(self.s.findTheDistanceValue([5], [10], 4), 1)
        self.assertEqual(self.s.findTheDistanceValue([5], [10], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(self.s.findTheDistanceValue([-1, -2], [-3, -4], 1), 1)

    def test_identical_arrays(self):
        self.assertEqual(self.s.findTheDistanceValue([5, 5, 5], [5, 5, 5], 0), 0)


if __name__ == "__main__":
    unittest.main()
