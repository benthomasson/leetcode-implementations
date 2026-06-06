"""Minimum Index Sum of Two Lists - LeetCode"""

import unittest


def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    """Find common strings with the least index sum.

    Args:
        list1: First list of unique strings.
        list2: Second list of unique strings.

    Returns:
        All common strings with the minimum index sum.
    """
    index_map = {s: i for i, s in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for j, s in enumerate(list2):
        if j > min_sum:
            break
        if s in index_map:
            idx_sum = index_map[s] + j
            if idx_sum < min_sum:
                min_sum = idx_sum
                result = [s]
            elif idx_sum == min_sum:
                result.append(s)

    return result


class TestFindRestaurant(unittest.TestCase):
    def test_single_common(self):
        self.assertEqual(
            findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
            ),
            ["Shogun"],
        )

    def test_multiple_common_different_sums(self):
        self.assertEqual(
            findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
            ),
            ["Shogun"],
        )

    def test_multiple_common_same_sum(self):
        result = findRestaurant(["happy", "sad", "good"], ["sad", "happy", "good"])
        self.assertEqual(sorted(result), sorted(["sad", "happy"]))

    def test_single_element_lists(self):
        self.assertEqual(findRestaurant(["a"], ["a"]), ["a"])

    def test_first_elements_match(self):
        self.assertEqual(findRestaurant(["a", "b"], ["a", "c"]), ["a"])

    def test_all_common(self):
        result = findRestaurant(["a", "b"], ["b", "a"])
        self.assertEqual(sorted(result), ["a", "b"])

    def test_early_termination(self):
        # Common string at index 0 in both lists - should terminate early
        self.assertEqual(
            findRestaurant(["x", "y", "z"], ["x", "y", "z"]),
            ["x"],
        )


if __name__ == "__main__":
    unittest.main()
