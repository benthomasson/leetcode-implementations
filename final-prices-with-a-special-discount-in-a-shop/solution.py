from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """Return final prices after applying first eligible discount.

        Args:
            prices: List of item prices.

        Returns:
            List of final prices after discounts.
        """
        result = prices[:]
        stack: List[int] = []  # indices of items awaiting discount

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                result[idx] = prices[idx] - price
            stack.append(i)

        return result
