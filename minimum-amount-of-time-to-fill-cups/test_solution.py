import unittest
from solution import min_seconds


class TestMinSeconds(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_seconds([1, 4, 2]), 4)

    def test_example2(self):
        self.assertEqual(min_seconds([5, 4, 4]), 7)

    def test_example3(self):
        self.assertEqual(min_seconds([5, 0, 0]), 5)

    def test_all_zeros(self):
        self.assertEqual(min_seconds([0, 0, 0]), 0)

    def test_single_nonzero(self):
        self.assertEqual(min_seconds([0, 3, 0]), 3)

    def test_equal_values(self):
        self.assertEqual(min_seconds([3, 3, 3]), 5)

    def test_large_values(self):
        self.assertEqual(min_seconds([100, 100, 100]), 150)

    def test_one_dominant(self):
        self.assertEqual(min_seconds([10, 1, 1]), 10)

    def test_two_zeros(self):
        self.assertEqual(min_seconds([7, 0, 0]), 7)

    def test_small_balanced(self):
        self.assertEqual(min_seconds([1, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()
