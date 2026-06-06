"""Two Sum III - Data Structure Design."""

from collections import Counter


class TwoSum:
    """Data structure that supports adding numbers and finding pairs that sum to a target."""

    def __init__(self):
        self.counts = Counter()

    def add(self, number: int) -> None:
        """Add a number to the data structure."""
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        """Return True if any pair of numbers sums to value."""
        for num in self.counts:
            complement = value - num
            if complement != num:
                if complement in self.counts:
                    return True
            else:
                if self.counts[num] >= 2:
                    return True
        return False
