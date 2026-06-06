class Solution:
    def num_rescue_boats(self, s: str) -> str:
        """Reverse only the English letters in a string, keeping other characters in place.

        Args:
            s: Input string containing letters and non-letter characters.

        Returns:
            String with only the English letters reversed.
        """
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
