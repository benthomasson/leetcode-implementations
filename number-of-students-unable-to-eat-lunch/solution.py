from collections import Counter


def countStudents(students: list[int], sandwiches: list[int]) -> int:
    """Return the number of students unable to eat lunch.

    Args:
        students: Preferences of students in queue (0 or 1).
        sandwiches: Stack of sandwiches, index 0 is top.

    Returns:
        Number of students that cannot eat.
    """
    count = Counter(students)
    for s in sandwiches:
        if count[s] == 0:
            return count[0] + count[1]
        count[s] -= 1
    return 0


# Alias per task requirements
min_time_to_remove_balloons = countStudents
