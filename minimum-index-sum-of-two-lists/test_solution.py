"""Tests for Minimum Index Sum of Two Lists."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import findRestaurant


class TestFindRestaurant(unittest.TestCase):
    # --- LeetCode examples ---
    def test_example1_single_common(self):
        self.assertEqual(
            findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
            ),
            ["Shogun"],
        )

    def test_example2_multiple_common_different_sums(self):
        self.assertEqual(
            findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
            ),
            ["Shogun"],
        )

    def test_example3_multiple_common_same_sum(self):
        result = findRestaurant(["happy", "sad", "good"], ["sad", "happy", "good"])
        self.assertEqual(sorted(result), sorted(["sad", "happy"]))

    # --- Edge cases ---
    def test_single_element_lists(self):
        self.assertEqual(findRestaurant(["a"], ["a"]), ["a"])

    def test_both_at_index_zero(self):
        self.assertEqual(findRestaurant(["x", "y"], ["x", "z"]), ["x"])

    def test_common_at_end(self):
        self.assertEqual(
            findRestaurant(["a", "b", "c"], ["d", "e", "c"]),
            ["c"],
        )

    def test_strings_with_spaces(self):
        result = findRestaurant(["hello world", "foo"], ["foo", "hello world"])
        self.assertEqual(sorted(result), sorted(["hello world", "foo"]))

    def test_large_lists_common_at_start(self):
        list1 = ["match"] + [f"a{i}" for i in range(999)]
        list2 = ["match"] + [f"b{i}" for i in range(999)]
        self.assertEqual(findRestaurant(list1, list2), ["match"])

    def test_no_early_termination_needed(self):
        # Common only at the last positions
        list1 = ["a", "b", "common"]
        list2 = ["x", "y", "common"]
        self.assertEqual(findRestaurant(list1, list2), ["common"])


if __name__ == "__main__":
    unittest.main()
