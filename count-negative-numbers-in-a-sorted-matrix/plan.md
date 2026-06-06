# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-negative-numbers-in-a-sorted-matrix":

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return _the number of **negative** numbers in_ `grid`.

**Example 1:**

**Input:** grid = \[\[4,3,2,-1\],\[3,2,1,-1\],\[1,1,-1,-2\],\[-1,-1,-2,-3\]\]
**Output:** 8
**Explanation:** There are 8 negatives number in the matrix.

**Example 2:**

**Input:** grid = \[\[3,2\],\[1,0\]\]
**Output:** 0

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 100`
*   `-100 <= grid[i][j] <= 100`

**Follow up:** Could you find an `O(n + m)` solution?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: balanced_string

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. 

**Summary:** Use the classic O(n + m) staircase traversal starting from the top-right corner of the matrix. Move left when a negative is found (counting all rows below), move down otherwise. Implementation needs `balanced_string` as the function name per requirements, with full docstring and comprehensive edge-case tests.

[Committed changes to planner branch]