# Plan (Iteration 1)

Task: Solve the LeetCode problem "pascals-triangle-ii":

Given an integer `rowIndex`, return the `rowIndexth` (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

**Example 1:**

**Input:** rowIndex = 3
**Output:** \[1,3,3,1\]

**Example 2:**

**Input:** rowIndex = 0
**Output:** \[1\]

**Example 3:**

**Input:** rowIndex = 1
**Output:** \[1,1\]

**Constraints:**

*   `0 <= rowIndex <= 33`

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: get_row

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is the classic in-place single-row update — simple, optimal, and well-suited for this problem.

[Committed changes to planner branch]