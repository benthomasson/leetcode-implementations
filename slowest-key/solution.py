from typing import List


def minInteger(releaseTimes: List[int], keysPressed: str) -> str:
    """Find the key with the longest press duration, breaking ties lexicographically.

    Args:
        releaseTimes: Sorted list of release times for each keypress.
        keysPressed: String of keys pressed in order.

    Returns:
        The key with the longest duration (lexicographically largest on tie).
    """
    best_key = keysPressed[0]
    best_dur = releaseTimes[0]

    for i in range(1, len(releaseTimes)):
        dur = releaseTimes[i] - releaseTimes[i - 1]
        if dur > best_dur or (dur == best_dur and keysPressed[i] > best_key):
            best_key = keysPressed[i]
            best_dur = dur

    return best_key
