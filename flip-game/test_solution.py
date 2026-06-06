import unittest
from solution import Solution


class TestGeneratePossibleNextMoves(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_four_pluses(self):
        self.assertCountEqual(
            self.s.generate_possible_next_moves("++++"),
            ["--++", "+--+", "++--"],
        )

    def test_single_plus(self):
        self.assertEqual(self.s.generate_possible_next_moves("+"), [])

    def test_two_minuses(self):
        self.assertEqual(self.s.generate_possible_next_moves("--"), [])

    def test_two_pluses(self):
        self.assertEqual(self.s.generate_possible_next_moves("++"), ["--"])

    def test_empty_string(self):
        self.assertEqual(self.s.generate_possible_next_moves(""), [])

    def test_embedded_pluses(self):
        self.assertCountEqual(
            self.s.generate_possible_next_moves("-+++-"),
            ["-+---", "---+-"],
        )

    def test_alternating(self):
        self.assertEqual(self.s.generate_possible_next_moves("+-+-"), [])

    def test_all_pluses(self):
        result = self.s.generate_possible_next_moves("+++")
        self.assertCountEqual(result, ["--+", "+--"])


if __name__ == "__main__":
    unittest.main()
