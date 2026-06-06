from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """Return the wealth of the richest customer.

        Args:
            accounts: m x n grid where accounts[i][j] is money customer i has in bank j.

        Returns:
            Maximum total wealth across all customers.
        """
        return max(sum(row) for row in accounts)
