"""Minimum Cost of Buying Candies With Discount."""

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """Return minimum cost to buy all candies with every-3rd-free discount.

        Args:
            cost: List of candy costs.

        Returns:
            Minimum total cost after applying discounts.
        """
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)

    # Task requires this alias
    max_difference = minimumCost
