import unittest
from solution import Solution


class TestMaximumRemovals(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maximumRemovals("XXX"), 1)

    def test_example2(self):
        self.assertEqual(self.sol.maximumRemovals("XXOX"), 2)

    def test_example3(self):
        self.assertEqual(self.sol.maximumRemovals("OOOO"), 0)

    def test_all_x(self):
        self.assertEqual(self.sol.maximumRemovals("XXXXXX"), 2)

    def test_all_o(self):
        self.assertEqual(self.sol.maximumRemovals("OOO"), 0)

    def test_single_x_start(self):
        self.assertEqual(self.sol.maximumRemovals("XOO"), 1)

    def test_single_x_end(self):
        self.assertEqual(self.sol.maximumRemovals("OOX"), 1)

    def test_single_x_middle(self):
        self.assertEqual(self.sol.maximumRemovals("OXO"), 1)

    def test_x_spaced_apart(self):
        self.assertEqual(self.sol.maximumRemovals("XOOOOX"), 2)

    def test_x_close_together(self):
        # X at 0, X at 2 -> first move covers 0-2, so 1 move
        self.assertEqual(self.sol.maximumRemovals("XOXOO"), 1)

    def test_min_length(self):
        self.assertEqual(self.sol.maximumRemovals("OOO"), 0)
        self.assertEqual(self.sol.maximumRemovals("XOO"), 1)

    def test_long_string(self):
        # 1000 X's -> ceil(1000/3) = 334 moves
        self.assertEqual(self.sol.maximumRemovals("X" * 1000), 334)

    def test_alternating(self):
        # XOXOXO -> X at 0: move, skip to 3 -> X at 4: move, skip to 7 -> done = 2
        self.assertEqual(self.sol.maximumRemovals("XOXOXO"), 2)


if __name__ == "__main__":
    unittest.main()
