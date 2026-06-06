class Solution:
    def totalMoney(self, n: int) -> int:
        """Calculate total money in Leetcode bank after n days.

        Args:
            n: Number of days.

        Returns:
            Total money saved.
        """
        full_weeks = n // 7
        remaining_days = n % 7
        # Sum of complete weeks: each week k (0-indexed) totals 28 + 7k
        weeks_total = full_weeks * 28 + 7 * full_weeks * (full_weeks - 1) // 2
        # Remaining days start at (full_weeks + 1) and increment by 1 each day
        days_total = remaining_days * (full_weeks + 1) + remaining_days * (remaining_days - 1) // 2
        return weeks_total + days_total
