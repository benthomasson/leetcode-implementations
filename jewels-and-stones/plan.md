# Plan (Iteration 1)

Task: Solve the LeetCode problem "jewels-and-stones":

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a "` is considered a different type of stone from `"A "`.

**Example 1:**

**Input:** jewels = "aA", stones = "aAAbbbb"
**Output:** 3

**Example 2:**

**Input:** jewels = "z", stones = "ZZ"
**Output:** 0

**Constraints:**

*   `1 <= jewels.length, stones.length <= 50`
*   `jewels` and `stones` consist of only English letters.
*   All the characters of `jewels` are **unique**.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: num_jewels_in_stones

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: set lookup + counting. Confidence is **HIGH**.

[Committed changes to planner branch]