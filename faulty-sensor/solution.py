from typing import List


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        """Determine which sensor is defective by finding the first mismatch
        and checking which shift hypothesis holds.

        Args:
            sensor1: Data points from sensor 1.
            sensor2: Data points from sensor 2.

        Returns:
            1 or 2 for the defective sensor, or -1 if indeterminate.
        """
        n = len(sensor1)
        i = 0
        while i < n and sensor1[i] == sensor2[i]:
            i += 1

        # No mismatch found — identical arrays
        if i >= n - 1:
            return -1

        # Check if sensor1 could be defective (sensor1 dropped a value at i)
        # sensor1[i+1:] should match sensor2[i:n-1]
        s1_bad = sensor1[i:n - 1] == sensor2[i + 1:]

        # Check if sensor2 could be defective (sensor2 dropped a value at i)
        # sensor1[i+1:] should match sensor2[i:n-1]
        s2_bad = sensor2[i:n - 1] == sensor1[i + 1:]

        if s1_bad == s2_bad:
            return -1
        return 1 if s1_bad else 2
