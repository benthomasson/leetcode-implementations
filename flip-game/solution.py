from typing import List


class Solution:
    def generate_possible_next_moves(self, currentState: str) -> List[str]:
        """Return all possible states after flipping one '++' to '--'.

        Args:
            currentState: String of '+' and '-' characters.

        Returns:
            List of strings representing all possible next states.
        """
        result = []
        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                result.append(currentState[:i] + "--" + currentState[i + 2:])
        return result
