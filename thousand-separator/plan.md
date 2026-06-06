# Plan (Iteration 1)

Task: Solve the LeetCode problem "thousand-separator":

Given an integer `n`, add a dot ( ". ") as the thousands separator and return it in string format.

**Example 1:**

**Input:** n = 987
**Output:**  "987 "

**Example 2:**

**Input:** n = 1234
**Output:**  "1.234 "

**Constraints:**

*   `0 <= n <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: can_be_equal

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward string chunking problem — reverse, group by 3, join with dots, reverse back.

[Committed changes to planner branch]