import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution


class TestNumEquivDominoPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        assert self.sol.num_equiv_domino_pairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1

    def test_example2(self):
        assert self.sol.num_equiv_domino_pairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3

    def test_single_domino(self):
        assert self.sol.num_equiv_domino_pairs([[1, 2]]) == 0

    def test_all_identical(self):
        # 4 identical → C(4,2) = 6
        assert self.sol.num_equiv_domino_pairs([[3, 4], [3, 4], [3, 4], [3, 4]]) == 6

    def test_all_unique(self):
        assert self.sol.num_equiv_domino_pairs([[1, 2], [3, 4], [5, 6], [7, 8]]) == 0

    def test_palindrome_dominoes(self):
        # [1,1] and [1,1] are equivalent
        assert self.sol.num_equiv_domino_pairs([[1, 1], [1, 1], [1, 1]]) == 3

    def test_rotated_pairs(self):
        # [2,3] and [3,2] are equivalent
        assert self.sol.num_equiv_domino_pairs([[2, 3], [3, 2]]) == 1

    def test_mixed_groups(self):
        # Two groups: (1,2) x3 → 3 pairs, (3,4) x2 → 1 pair = 4
        assert self.sol.num_equiv_domino_pairs([[1, 2], [2, 1], [1, 2], [3, 4], [4, 3]]) == 4


if __name__ == "__main__":
    unittest.main()
