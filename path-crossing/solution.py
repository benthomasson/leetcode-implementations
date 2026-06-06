"""Path Crossing problem solution."""


def lucky_numbers(path: str) -> bool:
    """Determine if a path crosses itself on a 2D plane.

    Args:
        path: String of 'N', 'S', 'E', 'W' directions.

    Returns:
        True if the path revisits any coordinate, False otherwise.
    """
    directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
    x, y = 0, 0
    visited = {(0, 0)}
    for char in path:
        dx, dy = directions[char]
        x += dx
        y += dy
        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False
