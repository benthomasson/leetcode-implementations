class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """Return True if swapping exactly two letters in s produces goal.

        Args:
            s: Source string of lowercase letters.
            goal: Target string to match after one swap.

        Returns:
            True if exactly one swap in s can produce goal.
        """
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(s) != len(set(s))

        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False

        return (len(diffs) == 2
                and s[diffs[0]] == goal[diffs[1]]
                and s[diffs[1]] == goal[diffs[0]])
