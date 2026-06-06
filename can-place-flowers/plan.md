# Plan (Iteration 1)

Task: Solve the LeetCode problem "can-place-flowers":

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` _if_ `n` _new flowers can be planted in the_ `flowerbed` _without violating the no-adjacent-flowers rule and_ `false` _otherwise_.

**Example 1:**

**Input:** flowerbed = \[1,0,0,0,1\], n = 1
**Output:** true

**Example 2:**

**Input:** flowerbed = \[1,0,0,0,1\], n = 2
**Output:** false

**Constraints:**

*   `1 <= flowerbed.length <= 2 * 104`
*   `flowerbed[i]` is `0` or `1`.
*   There are no two adjacent flowers in `flowerbed`.
*   `0 <= n <= flowerbed.length`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: canPlaceFlowers

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The greedy single-pass approach is the standard optimal solution for this problem — straightforward to implement and handles all edge cases cleanly.

[Committed changes to planner branch]