# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-cost-to-move-chips-to-the-same-position":

We have `n` chips, where the position of the `ith` chip is `position[i]`.

We need to move all the chips to **the same position**. In one step, we can change the position of the `ith` chip from `position[i]` to:

*   `position[i] + 2` or `position[i] - 2` with `cost = 0`.
*   `position[i] + 1` or `position[i] - 1` with `cost = 1`.

Return _the minimum cost_ needed to move all the chips to the same position.

**Example 1:**

**Input:** position = \[1,2,3\]
**Output:** 1
**Explanation:** First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

**Example 2:**

**Input:** position = \[2,2,2,3,3\]
**Output:** 2
**Explanation:** We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.

**Example 3:**

**Input:** position = \[1,1000000000\]
**Output:** 1

**Constraints:**

*   `1 <= position.length <= 100`
*   `1 <= position[i] <= 10^9`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sort_array

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

## SELF-REVIEW

1. **What went well:** Classic parity insight is straightforward — the problem is well-known and the optimal approach is clear.
2. **Missing info:** None needed. The task spec says function name should be `sort_array` (odd name for this problem, but we'll follow it).
3. **Next time:** Nothing to improve for problems this simple.
4. **Confidence:** **HIGH** — this is a textbook greedy/observation problem with a clean O(n) solution. No ambiguity in approach.

[Committed changes to planner branch]