# Plan (Iteration 1)

Task: Solve the LeetCode problem "special-positions-in-a-binary-matrix":

Given an `m x n` binary matrix `mat`, return _the number of special positions in_ `mat`_._

A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).

**Example 1:**

**Input:** mat = \[\[1,0,0\],\[0,0,1\],\[1,0,0\]\]
**Output:** 1
**Explanation:** (1, 2) is a special position because mat\[1\]\[2\] == 1 and all other elements in row 1 and column 2 are 0.

**Example 2:**

**Input:** mat = \[\[1,0,0\],\[0,1,0\],\[0,0,1\]\]
**Output:** 3
**Explanation:** (0, 0), (1, 1) and (2, 2) are special positions.

**Constraints:**

*   `m == mat.length`
*   `n == mat[i].length`
*   `1 <= m, n <= 100`
*   `mat[i][j]` is either `0` or `1`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is the canonical O(m×n) row/col sum method — simple and optimal for this problem.

[Committed changes to planner branch]