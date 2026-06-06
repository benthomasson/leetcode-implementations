"""Minimum Hours of Training to Win a Competition."""

from typing import List


def min_training_hours(
    initialEnergy: int,
    initialExperience: int,
    energy: List[int],
    experience: List[int],
) -> int:
    """Return minimum training hours to defeat all opponents.

    Args:
        initialEnergy: Starting energy level.
        initialExperience: Starting experience level.
        energy: Energy of each opponent in order.
        experience: Experience of each opponent in order.

    Returns:
        Minimum hours of training needed.
    """
    # Energy: need strictly greater than sum of all energy costs
    energy_needed = max(0, sum(energy) + 1 - initialEnergy)

    # Experience: simulate, adding training hours when current exp is insufficient
    exp_needed = 0
    cur_exp = initialExperience
    for exp in experience:
        if cur_exp <= exp:
            gap = exp + 1 - cur_exp
            exp_needed += gap
            cur_exp += gap
        cur_exp += exp

    return energy_needed + exp_needed
