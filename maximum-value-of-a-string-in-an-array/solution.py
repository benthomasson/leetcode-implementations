from typing import List


class Solution:
    def maxValue(self, strs: List[str]) -> int:
        """Return the maximum value among alphanumeric strings.

        Args:
            strs: List of alphanumeric strings.

        Returns:
            Maximum value, where digit-only strings use their numeric value
            and others use their length.
        """
        return max(int(s) if s.isdigit() else len(s) for s in strs)
