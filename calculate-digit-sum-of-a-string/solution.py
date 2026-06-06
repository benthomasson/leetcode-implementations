class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """Repeatedly replace groups of k digits with their digit sum until len(s) <= k.

        Args:
            s: String of digits.
            k: Group size.

        Returns:
            The final string after all rounds.
        """
        while len(s) > k:
            s = "".join(
                str(sum(int(c) for c in s[i:i + k]))
                for i in range(0, len(s), k)
            )
        return s
