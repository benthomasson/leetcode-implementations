import unittest
import sys
sys.path.insert(0, "../implementer")
from solution import minInteger


class TestMinInteger(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(minInteger([9, 29, 49, 50], "cbcd"), "c")

    def test_example2(self):
        self.assertEqual(minInteger([12, 23, 36, 46, 62], "spuda"), "a")

    # Edge cases
    def test_min_n(self):
        self.assertEqual(minInteger([5, 10], "az"), "z")

    def test_first_key_longest(self):
        self.assertEqual(minInteger([100, 101, 102], "xyz"), "x")

    def test_all_same_duration_picks_largest_letter(self):
        self.assertEqual(minInteger([10, 20, 30], "bac"), "c")

    def test_tie_picks_lexicographically_larger(self):
        self.assertEqual(minInteger([5, 10], "ba"), "b")

    def test_repeated_key_different_durations(self):
        self.assertEqual(minInteger([1, 100, 101], "aba"), "b")

    def test_last_key_longest(self):
        self.assertEqual(minInteger([1, 2, 100], "abc"), "c")

    def test_single_key_repeated(self):
        self.assertEqual(minInteger([10, 20], "aa"), "a")

    def test_large_release_times(self):
        self.assertEqual(minInteger([1000000000 - 1, 1000000000], "ab"), "a")


if __name__ == "__main__":
    unittest.main()
