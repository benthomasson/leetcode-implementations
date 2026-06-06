"""LeetCode: Destination City

Find the destination city — the city with no outgoing path.
"""

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """Find the destination city that has no outgoing path.

        Given directed paths between cities forming a line without loops,
        returns the city that never appears as a source (departure) city.

        Args:
            paths: List of [source, destination] city pairs. Each pair
                represents a direct path from source to destination.

        Returns:
            The destination city with no outgoing path.

        Raises:
            ValueError: If paths is empty.

        Examples:
            >>> s = Solution()
            >>> s.destCity([["London", "New York"],
            ...     ["New York", "Lima"], ["Lima", "Sao Paulo"]])
            'Sao Paulo'
            >>> s.destCity([["B", "C"], ["D", "B"],
            ...     ["C", "A"]])
            'A'
            >>> s.destCity([["A", "Z"]])
            'Z'
        """
        if not paths:
            raise ValueError("paths must not be empty")

        sources = {path[0] for path in paths}

        for path in paths:
            if path[1] not in sources:
                return path[1]

        # Should not be reached given problem guarantees
        return ""
