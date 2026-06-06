class Solution:
    def minTimeToType(self, word: str) -> int:
        """Return minimum seconds to type word on a circular typewriter."""
        time = 0
        curr = 0  # 'a'
        for ch in word:
            target = ord(ch) - ord('a')
            diff = abs(target - curr)
            time += min(diff, 26 - diff) + 1
            curr = target
        return time
