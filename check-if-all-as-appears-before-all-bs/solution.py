class Solution:
    def firstDayBeenInAllRooms(self, s: str) -> bool:
        """Check if all 'a's appear before all 'b's in the string.

        Args:
            s: String consisting only of 'a' and 'b'.

        Returns:
            True if every 'a' appears before every 'b', False otherwise.
        """
        return "ba" not in s
