# Plan (Iteration 1)

Task: Solve the LeetCode problem "check-if-matrix-is-x-matrix":

A square matrix is said to be an **X-Matrix** if **both** of the following conditions hold:

1.  All the elements in the diagonals of the matrix are **non-zero**.
2.  All other elements are 0.

Given a 2D integer array `grid` of size `n x n` representing a square matrix, return `true` _if_ `grid` _is an X-Matrix_. Otherwise, return `false`.

**Example 1:**

**Input:** grid = \[\[2,0,0,1\],\[0,3,1,0\],\[0,5,2,0\],\[4,0,0,2\]\]
**Output:** true
**Explanation:** Refer to the diagram above. 
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is an X-Matrix.

**Example 2:**

**Input:** grid = \[\[5,7,0\],\[0,3,1\],\[0,5,0\]\]
**Output:** false
**Explanation:** Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is not an X-Matrix.

**Constraints:**

*   `n == grid.length == grid[i].length`
*   `3 <= n <= 100`
*   `0 <= grid[i][j] <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: longest_repeat_substring

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Single-pass O(n²) iteration — check each cell is non-zero if on a diagonal, zero otherwise. Early return on first violation. Straightforward implementation with tests covering both examples and edge cases. High confidence.

[Committed changes to planner branch]