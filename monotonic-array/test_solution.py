import unittest
from solution import Solution


class TestIsMonotonic(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_increasing(self):
        self.assertTrue(self.s.isMonotonic([1, 2, 2, 3]))

    def test_decreasing(self):
        self.assertTrue(self.s.isMonotonic([6, 5, 4, 4]))

    def test_not_monotonic(self):
        self.assertFalse(self.s.isMonotonic([1, 3, 2]))

    def test_single_element(self):
        self.assertTrue(self.s.isMonotonic([1]))

    def test_two_elements_increasing(self):
        self.assertTrue(self.s.isMonotonic([1, 2]))

    def test_two_elements_decreasing(self):
        self.assertTrue(self.s.isMonotonic([2, 1]))

    def test_all_equal(self):
        self.assertTrue(self.s.isMonotonic([3, 3, 3, 3]))

    def test_strictly_increasing(self):
        self.assertTrue(self.s.isMonotonic([1, 2, 3, 4, 5]))

    def test_strictly_decreasing(self):
        self.assertTrue(self.s.isMonotonic([5, 4, 3, 2, 1]))

    def test_peak(self):
        self.assertFalse(self.s.isMonotonic([1, 2, 3, 2, 1]))

    def test_valley(self):
        self.assertFalse(self.s.isMonotonic([3, 2, 1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
