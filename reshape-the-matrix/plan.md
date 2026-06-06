# Plan (Iteration 1)

Task: Solve the LeetCode problem "reshape-the-matrix":

In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new one with a different size `r x c` keeping its original data.

You are given an `m x n` matrix `mat` and two integers `r` and `c` representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the `reshape` operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

**Example 1:**

**Input:** mat = \[\[1,2\],\[3,4\]\], r = 1, c = 4
**Output:** \[\[1,2,3,4\]\]

**Example 2:**

**Input:** mat = \[\[1,2\],\[3,4\]\], r = 2, c = 4
**Output:** \[\[1,2\],\[3,4\]\]

**Constraints:**

*   `m == mat.length`
*   `n == mat[i].length`
*   `1 <= m, n <= 100`
*   `-1000 <= mat[i][j] <= 1000`
*   `1 <= r, c <= 300`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: matrixReshape

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: validate dimensions, flatten, slice into new rows. O(m×n) time and space.

[Committed changes to planner branch]