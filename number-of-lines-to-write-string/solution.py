from typing import List


class Solution:
    def numberOfWays(self, widths: List[int], s: str) -> List[int]:
        """Write string across lines of max 100 pixels, return [lines, last_line_width].

        Args:
            widths: Width in pixels for each letter a-z.
            s: String of lowercase English letters to write.

        Returns:
            List of [total_lines, width_of_last_line].
        """
        lines = 1
        current_width = 0

        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if current_width + w > 100:
                lines += 1
                current_width = w
            else:
                current_width += w

        return [lines, current_width]
