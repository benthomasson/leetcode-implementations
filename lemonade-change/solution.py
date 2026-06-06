from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """Determine if correct change can be given to every customer.

        Args:
            bills: List of bill values ($5, $10, or $20) from each customer.

        Returns:
            True if every customer can receive correct change, False otherwise.
        """
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:  # bill == 20
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
