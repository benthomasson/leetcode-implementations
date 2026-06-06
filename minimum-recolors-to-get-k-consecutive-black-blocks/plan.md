# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-recolors-to-get-k-consecutive-black-blocks":

You are given a **0-indexed** string `blocks` of length `n`, where `blocks[i]` is either `'W'` or `'B'`, representing the color of the `ith` block. The characters `'W'` and `'B'` denote the colors white and black, respectively.

You are also given an integer `k`, which is the desired number of **consecutive** black blocks.

In one operation, you can **recolor** a white block such that it becomes a black block.

Return _the **minimum** number of operations needed such that there is at least **one** occurrence of_ `k` _consecutive black blocks._

**Example 1:**

**Input:** blocks =  "WBBWWBBWBW ", k = 7
**Output:** 3
**Explanation:**
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks =  "BBBBBBBWBW ". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

**Example 2:**

**Input:** blocks =  "WBWBBBW ", k = 2
**Output:** 0
**Explanation:**
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

**Constraints:**

*   `n == blocks.length`
*   `1 <= n <= 100`
*   `blocks[i]` is either `'W'` or `'B'`.
*   `1 <= k <= n`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: min_operations

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Sliding window, O(n) time, O(1) space — count W's in each k-sized window and return the minimum.

[Committed changes to planner branch]