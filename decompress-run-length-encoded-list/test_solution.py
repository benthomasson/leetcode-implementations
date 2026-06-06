import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution

import unittest


class TestAddRooms(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.add_rooms([1, 2, 3, 4]), [2, 4, 4, 4])

    def test_example2(self):
        self.assertEqual(self.sol.add_rooms([1, 1, 2, 3]), [1, 3, 3])

    def test_single_pair(self):
        self.assertEqual(self.sol.add_rooms([5, 1]), [1, 1, 1, 1, 1])

    def test_minimum_input(self):
        self.assertEqual(self.sol.add_rooms([1, 1]), [1])

    def test_max_frequency(self):
        self.assertEqual(self.sol.add_rooms([100, 42]), [42] * 100)

    def test_all_freq_one(self):
        self.assertEqual(self.sol.add_rooms([1, 5, 1, 6, 1, 7]), [5, 6, 7])

    def test_same_values(self):
        self.assertEqual(self.sol.add_rooms([2, 3, 3, 3]), [3, 3, 3, 3, 3])

    def test_max_values(self):
        self.assertEqual(self.sol.add_rooms([100, 100]), [100] * 100)


if __name__ == '__main__':
    unittest.main()
