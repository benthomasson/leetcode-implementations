from collections import Counter
from typing import List


class Solution:
    def num_equiv_domino_pairs(self, dominoes: List[List[int]]) -> int:
        """Count the number of equivalent domino pairs.

        Args:
            dominoes: List of domino pairs [a, b] where 1 <= a, b <= 9.

        Returns:
            Number of pairs (i, j) with i < j where dominoes[i] is equivalent to dominoes[j].
        """
        counts = Counter((min(a, b), max(a, b)) for a, b in dominoes)
        return sum(n * (n - 1) // 2 for n in counts.values())
