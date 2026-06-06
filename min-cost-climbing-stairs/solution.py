from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Find minimum cost to reach the top of the staircase.

        Args:
            cost: Cost of each step. Length >= 2.

        Returns:
            Minimum total cost to reach the top.
        """
        prev2, prev1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
        return min(prev1, prev2)
