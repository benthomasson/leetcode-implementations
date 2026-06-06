class Solution:
    def confusingNumber(self, n: int) -> bool:
        """Return True if n is a confusing number (rotated 180 degrees gives a different valid number)."""
        rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        original = n
        rotated = 0
        while n > 0:
            digit = n % 10
            if digit not in rotate:
                return False
            rotated = rotated * 10 + rotate[digit]
            n //= 10
        return rotated != original
