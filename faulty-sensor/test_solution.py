import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution

import unittest


class TestBadSensor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.sol.badSensor([2, 3, 4, 5], [2, 1, 3, 4]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.badSensor([2, 2, 2, 2, 2], [2, 2, 2, 2, 5]), -1)

    def test_example3(self):
        self.assertEqual(self.sol.badSensor([2, 3, 2, 2, 3, 2], [2, 3, 2, 3, 2, 7]), 2)

    # --- Edge cases ---
    def test_identical_arrays(self):
        self.assertEqual(self.sol.badSensor([1, 2, 3], [1, 2, 3]), -1)

    def test_single_element(self):
        self.assertEqual(self.sol.badSensor([1], [1]), -1)

    def test_two_elements_differ_at_last(self):
        # Only differ at last element — indeterminate
        self.assertEqual(self.sol.badSensor([1, 2], [1, 3]), -1)

    def test_mismatch_at_start_sensor1_bad(self):
        # sensor1 dropped index 0: correct=[5,1,2,3], sensor1=[1,2,3,9], sensor2=[5,1,2,3]
        self.assertEqual(self.sol.badSensor([1, 2, 3, 9], [5, 1, 2, 3]), 1)

    def test_mismatch_at_start_sensor2_bad(self):
        # sensor2 dropped index 0: correct=[5,1,2,3], sensor2=[1,2,3,9], sensor1=[5,1,2,3]
        self.assertEqual(self.sol.badSensor([5, 1, 2, 3], [1, 2, 3, 9]), 2)

    def test_ambiguous_both_hypotheses_hold(self):
        # Both shift hypotheses valid — return -1
        self.assertEqual(self.sol.badSensor([1, 1, 1, 1, 2], [1, 1, 1, 1, 3]), -1)


if __name__ == '__main__':
    unittest.main()
