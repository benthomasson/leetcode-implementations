import unittest
from solution import find_missing_ranges


class TestFindMissingRanges(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            find_missing_ranges([0, 1, 3, 50, 75], 0, 99),
            ["2", "4->49", "51->74", "76->99"],
        )

    def test_example2(self):
        self.assertEqual(find_missing_ranges([-1], -1, -1), [])

    def test_empty_nums(self):
        self.assertEqual(find_missing_ranges([], 1, 1), ["1"])
        self.assertEqual(find_missing_ranges([], 1, 5), ["1->5"])

    def test_no_missing(self):
        self.assertEqual(find_missing_ranges([1, 2, 3], 1, 3), [])

    def test_all_missing(self):
        self.assertEqual(find_missing_ranges([], -3, 3), ["-3->3"])

    def test_single_missing_at_start(self):
        self.assertEqual(find_missing_ranges([2, 3], 1, 3), ["1"])

    def test_single_missing_at_end(self):
        self.assertEqual(find_missing_ranges([1, 2], 1, 3), ["3"])

    def test_single_missing_in_middle(self):
        self.assertEqual(find_missing_ranges([1, 3], 1, 3), ["2"])

    def test_negatives(self):
        self.assertEqual(
            find_missing_ranges([-3, -1, 1], -5, 5),
            ["-5->-4", "-2", "0", "2->5"],
        )

    def test_lower_equals_upper_missing(self):
        self.assertEqual(find_missing_ranges([], 0, 0), ["0"])

    def test_lower_equals_upper_present(self):
        self.assertEqual(find_missing_ranges([0], 0, 0), [])


if __name__ == "__main__":
    unittest.main()
