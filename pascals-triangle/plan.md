# Plan (Iteration 1)

Task: Solve the LeetCode problem "pascals-triangle":

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

**Example 1:**

**Input:** numRows = 5
**Output:** \[\[1\],\[1,1\],\[1,2,1\],\[1,3,3,1\],\[1,4,6,4,1\]\]

**Example 2:**

**Input:** numRows = 1
**Output:** \[\[1\]\]

**Constraints:**

*   `1 <= numRows <= 30`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: generate

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple iterative approach — build each row from the previous one. O(n²) time/space, which is optimal.

[Committed changes to planner branch]