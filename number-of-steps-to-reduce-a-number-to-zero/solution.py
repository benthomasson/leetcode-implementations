class Solution:
    def queensAttacktheKing(self, num: int) -> int:
        """Return the number of steps to reduce num to zero.

        Args:
            num: Non-negative integer to reduce.

        Returns:
            Number of steps (divide by 2 if even, subtract 1 if odd).
        """
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

    numberOfSteps = queensAttacktheKing
