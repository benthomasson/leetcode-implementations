"""Maximum Units on a Truck - Greedy Solution."""


def busiest_servers(boxTypes: list[list[int]], truckSize: int) -> int:
    """Return the maximum total units that can be loaded onto a truck.

    Args:
        boxTypes: List of [numberOfBoxes, numberOfUnitsPerBox] pairs.
        truckSize: Maximum number of boxes the truck can carry.

    Returns:
        Maximum total number of units.
    """
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    remaining = truckSize
    for num_boxes, units_per_box in boxTypes:
        take = min(num_boxes, remaining)
        total_units += take * units_per_box
        remaining -= take
        if remaining == 0:
            break
    return total_units
