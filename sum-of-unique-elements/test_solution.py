import unittest
from solution import Solution


class TestSumOfUniqueElements(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.bestTeamScore([1, 2, 3, 2]), 4)

    def test_example2(self):
        self.assertEqual(self.s.bestTeamScore([1, 1, 1, 1, 1]), 0)

    def test_example3(self):
        self.assertEqual(self.s.bestTeamScore([1, 2, 3, 4, 5]), 15)

    def test_single_element(self):
        self.assertEqual(self.s.bestTeamScore([5]), 5)

    def test_all_duplicates(self):
        self.assertEqual(self.s.bestTeamScore([2, 2, 3, 3]), 0)

    def test_boundary_values(self):
        self.assertEqual(self.s.bestTeamScore([1, 100]), 101)

    def test_mix_unique_and_duplicate(self):
        self.assertEqual(self.s.bestTeamScore([1, 1, 2, 3, 3, 4]), 6)


if __name__ == "__main__":
    unittest.main()
