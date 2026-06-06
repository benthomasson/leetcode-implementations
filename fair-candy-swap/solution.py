class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        """Find candy boxes to swap so Alice and Bob have equal totals.

        Args:
            aliceSizes: Candy counts in each of Alice's boxes.
            bobSizes: Candy counts in each of Bob's boxes.

        Returns:
            [a, b] where a is Alice's box to give and b is Bob's box to give.
        """
        delta = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_set = set(bobSizes)
        for a in aliceSizes:
            if a - delta in bob_set:
                return [a, a - delta]
