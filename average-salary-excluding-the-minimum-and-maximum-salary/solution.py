from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        """Return average salary excluding the minimum and maximum.

        Args:
            salary: List of unique integer salaries (length >= 3).

        Returns:
            Average of all salaries except the min and max.
        """
        total = sum(salary)
        return (total - min(salary) - max(salary)) / (len(salary) - 2)
