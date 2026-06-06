from collections import Counter
from functools import reduce
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        """Return True if deck can be partitioned into groups of size x > 1 with matching values."""
        counts = Counter(deck).values()
        return reduce(gcd, counts) >= 2
