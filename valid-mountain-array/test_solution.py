import unittest
from solution import Solution


class TestValidMountainArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_too_short(self):
        self.assertFalse(self.s.validMountainArray([]))
        self.assertFalse(self.s.validMountainArray([1]))
        self.assertFalse(self.s.validMountainArray([1, 2]))

    def test_example_false_short(self):
        self.assertFalse(self.s.validMountainArray([2, 1]))

    def test_example_plateau(self):
        self.assertFalse(self.s.validMountainArray([3, 5, 5]))

    def test_example_valid(self):
        self.assertTrue(self.s.validMountainArray([0, 3, 2, 1]))

    def test_monotonically_increasing(self):
        self.assertFalse(self.s.validMountainArray([1, 2, 3, 4]))

    def test_monotonically_decreasing(self):
        self.assertFalse(self.s.validMountainArray([4, 3, 2, 1]))

    def test_peak_at_start(self):
        self.assertFalse(self.s.validMountainArray([5, 3, 1]))

    def test_peak_at_end(self):
        self.assertFalse(self.s.validMountainArray([1, 3, 5]))

    def test_minimum_valid(self):
        self.assertTrue(self.s.validMountainArray([1, 2, 1]))

    def test_all_equal(self):
        self.assertFalse(self.s.validMountainArray([3, 3, 3]))

    def test_larger_valid(self):
        self.assertTrue(self.s.validMountainArray([0, 1, 2, 3, 4, 3, 2, 1, 0]))

    def test_plateau_in_middle(self):
        self.assertFalse(self.s.validMountainArray([1, 3, 3, 2]))


if __name__ == "__main__":
    unittest.main()
