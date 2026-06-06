"""Categorize box according to criteria."""


def boxCategory(length: int, width: int, height: int, mass: int) -> str:
    """Categorize a box as Bulky, Heavy, Both, or Neither.

    Args:
        length: Box length.
        width: Box width.
        height: Box height.
        mass: Box mass.

    Returns:
        Category string with trailing space.
    """
    bulky = any(d >= 10_000 for d in (length, width, height)) or length * width * height >= 10**9
    heavy = mass >= 100

    if bulky and heavy:
        return "Both "
    if bulky:
        return "Bulky "
    if heavy:
        return "Heavy "
    return "Neither "
