import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution
import unittest


class TestXorOperation(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findTheDistanceValue(5, 0), 8)

    def test_example2(self):
        self.assertEqual(self.s.findTheDistanceValue(4, 3), 8)

    def test_single_element(self):
        # n=1, start=5 -> [5] -> 5
        self.assertEqual(self.s.findTheDistanceValue(1, 5), 5)

    def test_single_element_zero(self):
        # n=1, start=0 -> [0] -> 0
        self.assertEqual(self.s.findTheDistanceValue(1, 0), 0)

    def test_two_elements(self):
        # n=2, start=3 -> [3, 5] -> 3^5 = 6
        self.assertEqual(self.s.findTheDistanceValue(2, 3), 6)

    def test_start_zero_even_n(self):
        # n=4, start=0 -> [0,2,4,6] -> 0^2^4^6 = 0^2=2, 2^4=6, 6^6=0
        self.assertEqual(self.s.findTheDistanceValue(4, 0), 0)

    def test_large_n(self):
        # n=1000, start=0 — just verify it runs and returns an int
        result = self.s.findTheDistanceValue(1000, 0)
        self.assertIsInstance(result, int)

    def test_max_start(self):
        # n=1, start=1000 -> [1000] -> 1000
        self.assertEqual(self.s.findTheDistanceValue(1, 1000), 1000)

    def test_known_value_n3(self):
        # n=3, start=1 -> [1,3,5] -> 1^3=2, 2^5=7
        self.assertEqual(self.s.findTheDistanceValue(3, 1), 7)


if __name__ == '__main__':
    unittest.main()
