"""Maximum Score After Splitting a String."""


def max_score_after_splitting(s: str) -> int:
    """Return max score from splitting s into two non-empty parts.

    Score = zeros in left + ones in right.

    Args:
        s: String of '0' and '1' characters, length >= 2.

    Returns:
        Maximum score across all valid split positions.
    """
    ones_right = s.count("1")
    zeros_left = 0
    max_score = 0

    for i in range(len(s) - 1):  # split after index i; both parts non-empty
        if s[i] == "0":
            zeros_left += 1
        else:
            ones_right -= 1
        max_score = max(max_score, zeros_left + ones_right)

    return max_score
