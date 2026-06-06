# Plan (Iteration 1)

Task: Solve the LeetCode problem "delete-greatest-value-in-each-row":

You are given an `m x n` matrix `grid` consisting of positive integers.

Perform the following operation until `grid` becomes empty:

*   Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
*   Add the maximum of deleted elements to the answer.

**Note** that the number of columns decreases by one after each operation.

Return _the answer after performing the operations described above_.

**Example 1:**

**Input:** grid = \[\[1,2,4\],\[3,3,1\]\]
**Output:** 8
**Explanation:** The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

**Example 2:**

**Input:** grid = \[\[10\]\]
**Output:** 10
**Explanation:** The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 50`
*   `1 <= grid[i][j] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maxValueAfterOperations

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Sort each row, then sum the column-wise maximums. O(m·n·log n) time, O(1) extra space. The sorting aligns each row so that column `j` holds the j-th smallest value, making the "delete greatest" operation equivalent to just reading columns after sorting.

[Committed changes to planner branch]