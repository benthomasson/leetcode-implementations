import unittest
from solution import find_relative_ranks


class TestFindRelativeRanks(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            find_relative_ranks([5, 4, 3, 2, 1]),
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
        )

    def test_example2(self):
        self.assertEqual(
            find_relative_ranks([10, 3, 8, 9, 4]),
            ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
        )

    def test_single_element(self):
        self.assertEqual(find_relative_ranks([42]), ["Gold Medal"])

    def test_two_elements(self):
        self.assertEqual(find_relative_ranks([1, 2]), ["Silver Medal", "Gold Medal"])

    def test_three_elements(self):
        self.assertEqual(
            find_relative_ranks([3, 1, 2]),
            ["Gold Medal", "Bronze Medal", "Silver Medal"],
        )

    def test_ascending_order(self):
        self.assertEqual(
            find_relative_ranks([1, 2, 3, 4, 5]),
            ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"],
        )

    def test_zero_score(self):
        self.assertEqual(
            find_relative_ranks([0, 1000000]),
            ["Silver Medal", "Gold Medal"],
        )

    def test_four_elements(self):
        self.assertEqual(
            find_relative_ranks([8, 2, 9, 4]),
            ["Silver Medal", "4", "Gold Medal", "Bronze Medal"],
        )


if __name__ == "__main__":
    unittest.main()
