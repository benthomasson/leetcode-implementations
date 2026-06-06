class Solution:
    def reverseVowels(self, s: str) -> str:
        """Reverse only the vowels in a string using two pointers.

        Args:
            s: Input string of printable ASCII characters.

        Returns:
            String with vowels reversed.
        """
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
