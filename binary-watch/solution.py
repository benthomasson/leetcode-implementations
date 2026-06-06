"""Binary Watch - LeetCode solution."""


def readBinaryWatch(turnedOn: int) -> list[str]:
    """Return all possible times a binary watch could show with turnedOn LEDs lit.

    Args:
        turnedOn: Number of LEDs currently on (0-10).

    Returns:
        List of time strings in "h:mm" format.
    """
    return [
        f"{h}:{m:02d}"
        for h in range(12)
        for m in range(60)
        if bin(h).count("1") + bin(m).count("1") == turnedOn
    ]
