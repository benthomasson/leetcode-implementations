"""Student Attendance Record I - LeetCode 551."""


class Solution:
    def checkRecord(self, s: str) -> bool:
        """Check if student is eligible for attendance award.

        Args:
            s: Attendance record string of 'A', 'L', 'P' characters.

        Returns:
            True if fewer than 2 absences and no 3+ consecutive lates.
        """
        absences = 0
        consecutive_lates = 0

        for c in s:
            if c == 'A':
                absences += 1
                if absences >= 2:
                    return False
                consecutive_lates = 0
            elif c == 'L':
                consecutive_lates += 1
                if consecutive_lates >= 3:
                    return False
            else:
                consecutive_lates = 0

        return True
