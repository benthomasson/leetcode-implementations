# Plan (Iteration 1)

Task: Solve the LeetCode problem "lucky-numbers-in-a-matrix":

Given an `m x n` matrix of **distinct** numbers, return _all **lucky numbers** in the matrix in **any** order_.

A **lucky number** is an element of the matrix such that it is the minimum element in its row and maximum in its column.

**Example 1:**

**Input:** matrix = \[\[3,7,8\],\[9,11,13\],\[15,16,17\]\]
**Output:** \[15\]
**Explanation:** 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

**Example 2:**

**Input:** matrix = \[\[1,10,4,2\],\[9,3,8,7\],\[15,16,17,12\]\]
**Output:** \[12\]
**Explanation:** 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

**Example 3:**

**Input:** matrix = \[\[7,8\],\[1,2\]\]
**Output:** \[7\]
**Explanation:** 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

**Constraints:**

*   `m == mat.length`
*   `n == mat[i].length`
*   `1 <= n, m <= 50`
*   `1 <= matrix[i][j] <= 105`.
*   All elements in the matrix are distinct.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: dfs

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is straightforward: O(m×n) scan finding row minimums and checking if they're column maximums. The `dfs` function name is required but the algorithm is a simple linear scan, not a graph traversal.

[Committed changes to planner branch]