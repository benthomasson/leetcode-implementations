"""How Many Apples Can You Put into the Basket - LeetCode 1196."""

import unittest


def maxNumberOfApples(weight: list[int]) -> int:
    """Return max number of apples fitting in a basket with 5000 weight capacity.

    Args:
        weight: List of apple weights.

    Returns:
        Maximum number of apples that fit without exceeding 5000 total weight.
    """
    weight.sort()
    total = 0
    for i, w in enumerate(weight):
        total += w
        if total > 5000:
            return i
    return len(weight)


class TestMaxNumberOfApples(unittest.TestCase):
    def test_example1_all_fit(self):
        self.assertEqual(maxNumberOfApples([100, 200, 150, 1000]), 4)

    def test_example2_one_excluded(self):
        self.assertEqual(maxNumberOfApples([900, 950, 800, 1000, 700, 800]), 5)

    def test_single_apple_fits(self):
        self.assertEqual(maxNumberOfApples([5000]), 1)

    def test_single_apple_too_heavy(self):
        self.assertEqual(maxNumberOfApples([5001]), 0)

    def test_exact_capacity(self):
        self.assertEqual(maxNumberOfApples([1000, 1000, 1000, 1000, 1000]), 5)

    def test_none_fit(self):
        self.assertEqual(maxNumberOfApples([5001, 5002, 5003]), 0)

    def test_all_equal_weights(self):
        self.assertEqual(maxNumberOfApples([1000] * 6), 5)

    def test_all_weight_one(self):
        self.assertEqual(maxNumberOfApples([1] * 1000), 1000)


if __name__ == "__main__":
    unittest.main()
