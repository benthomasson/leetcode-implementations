from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        """Calculate diet plan performance points using a sliding window.

        Args:
            calories: Daily calorie consumption.
            k: Window size (consecutive days).
            lower: Lower threshold for losing a point.
            upper: Upper threshold for gaining a point.

        Returns:
            Total points after evaluating all windows.
        """
        points = 0
        window = sum(calories[:k])

        if window < lower:
            points -= 1
        elif window > upper:
            points += 1

        for i in range(k, len(calories)):
            window += calories[i] - calories[i - k]
            if window < lower:
                points -= 1
            elif window > upper:
                points += 1

        return points
