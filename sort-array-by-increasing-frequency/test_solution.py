import unittest
import sys
sys.path.insert(0, "../implementer")
from solution import num_sub


class TestNumSub(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(num_sub([1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2])

    def test_example2(self):
        self.assertEqual(num_sub([2, 3, 1, 3, 2]), [1, 3, 3, 2, 2])

    def test_example3(self):
        self.assertEqual(num_sub([-1, 1, -6, 4, 5, -6, 1, 4, 1]), [5, -1, 4, 4, -6, -6, 1, 1, 1])

    def test_single_element(self):
        self.assertEqual(num_sub([42]), [42])

    def test_all_same(self):
        self.assertEqual(num_sub([5, 5, 5]), [5, 5, 5])

    def test_all_unique_descending(self):
        self.assertEqual(num_sub([3, 1, 2]), [3, 2, 1])

    def test_negatives_tie(self):
        # freq: {-1:2, -2:2} → tie, decreasing value: -1 > -2 → [-1,-1,-2,-2]
        self.assertEqual(num_sub([-1, -2, -1, -2]), [-1, -1, -2, -2])

    def test_boundary_values(self):
        # Min/max constraint values
        self.assertEqual(num_sub([-100, 100]), [100, -100])

    def test_two_frequencies(self):
        # 4 appears once, 1 appears 3 times
        self.assertEqual(num_sub([1, 4, 1, 1]), [4, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
