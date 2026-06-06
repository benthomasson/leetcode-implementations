class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """Return list of FizzBuzz results from 1 to n.

        Args:
            n: Upper bound (inclusive).

        Returns:
            List of strings with Fizz/Buzz/FizzBuzz substitutions.
        """
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
