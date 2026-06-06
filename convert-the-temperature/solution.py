class Solution:
    def convert_temperature(self, celsius: float) -> list[float]:
        """Convert Celsius to Kelvin and Fahrenheit.

        Args:
            celsius: Temperature in Celsius (0 <= celsius <= 1000).

        Returns:
            List of [kelvin, fahrenheit].
        """
        return [celsius + 273.15, celsius * 1.80 + 32.00]
