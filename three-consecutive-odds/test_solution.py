import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import Solution


class TestThreeConsecutiveOdds(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # Problem examples
    def test_example1_no_consecutive(self):
        self.assertFalse(self.s.threeConsecutiveOdds([2, 6, 4, 1]))

    def test_example2_has_consecutive(self):
        self.assertTrue(self.s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))

    # Edge cases
    def test_single_element(self):
        self.assertFalse(self.s.threeConsecutiveOdds([1]))

    def test_two_odds(self):
        self.assertFalse(self.s.threeConsecutiveOdds([1, 3]))

    def test_exactly_three_odds(self):
        self.assertTrue(self.s.threeConsecutiveOdds([1, 3, 5]))

    def test_all_even(self):
        self.assertFalse(self.s.threeConsecutiveOdds([2, 4, 6, 8]))

    def test_three_odds_at_end(self):
        self.assertTrue(self.s.threeConsecutiveOdds([2, 4, 1, 3, 5]))

    def test_two_odds_broken_by_even(self):
        self.assertFalse(self.s.threeConsecutiveOdds([1, 3, 2, 1, 3]))

    def test_all_odds(self):
        self.assertTrue(self.s.threeConsecutiveOdds([1, 3, 5, 7, 9]))

    def test_max_values(self):
        self.assertTrue(self.s.threeConsecutiveOdds([999, 999, 999]))


if __name__ == '__main__':
    unittest.main()
