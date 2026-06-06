import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import pillowHolder
import unittest


class TestPillowHolder(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(pillowHolder(4, 5), 2)

    def test_example2(self):
        self.assertEqual(pillowHolder(3, 2), 3)

    def test_time_zero(self):
        self.assertEqual(pillowHolder(4, 0), 1)

    def test_pillow_at_end(self):
        self.assertEqual(pillowHolder(4, 3), 4)

    def test_full_round_trip(self):
        # 1->2->3->4->3->2->1 = 6 seconds, back to 1
        self.assertEqual(pillowHolder(4, 6), 1)

    def test_n2_bouncing(self):
        self.assertEqual(pillowHolder(2, 1), 2)
        self.assertEqual(pillowHolder(2, 2), 1)
        self.assertEqual(pillowHolder(2, 3), 2)

    def test_max_constraints(self):
        self.assertEqual(pillowHolder(1000, 1000), 999)

    def test_multiple_cycles(self):
        # n=4, cycle=3, time=9 -> 3 full passes (odd), remainder=0 -> 4
        self.assertEqual(pillowHolder(4, 9), 4)


if __name__ == '__main__':
    unittest.main()
