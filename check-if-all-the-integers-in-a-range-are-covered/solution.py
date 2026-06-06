class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        """Check if all integers in [left, right] are covered by at least one range.

        Args:
            ranges: List of [start, end] inclusive intervals.
            left: Left bound of query range.
            right: Right bound of query range.

        Returns:
            True if every integer in [left, right] is covered.
        """
        covered = [False] * 51
        for start, end in ranges:
            for i in range(start, end + 1):
                covered[i] = True
        return all(covered[i] for i in range(left, right + 1))
