import unittest
from solution import sumEvenGrandparent


class TestArrayTransformation(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sumEvenGrandparent([6, 2, 3, 4]), [6, 3, 3, 4])

    def test_example2(self):
        self.assertEqual(sumEvenGrandparent([1, 6, 3, 4, 3, 5]), [1, 4, 4, 4, 4, 5])

    def test_already_stable(self):
        self.assertEqual(sumEvenGrandparent([1, 2, 3]), [1, 2, 3])

    def test_all_equal(self):
        self.assertEqual(sumEvenGrandparent([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_length_3_valley(self):
        self.assertEqual(sumEvenGrandparent([5, 1, 5]), [5, 5, 5])

    def test_length_3_peak(self):
        self.assertEqual(sumEvenGrandparent([1, 5, 1]), [1, 1, 1])

    def test_monotonic_increasing(self):
        self.assertEqual(sumEvenGrandparent([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_monotonic_decreasing(self):
        self.assertEqual(sumEvenGrandparent([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])

    def test_single_peak(self):
        self.assertEqual(sumEvenGrandparent([1, 1, 100, 1, 1]), [1, 1, 1, 1, 1])

    def test_single_valley(self):
        self.assertEqual(sumEvenGrandparent([100, 100, 1, 100, 100]), [100, 100, 100, 100, 100])


if __name__ == "__main__":
    unittest.main()
