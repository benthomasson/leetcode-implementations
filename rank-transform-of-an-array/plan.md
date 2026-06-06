# Plan (Iteration 1)

Task: Solve the LeetCode problem "rank-transform-of-an-array":

Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

*   Rank is an integer starting from 1.
*   The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
*   Rank should be as small as possible.

**Example 1:**

**Input:** arr = \[40,10,20,30\]
**Output:** \[4,1,2,3\]
**Explanation**: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

**Example 2:**

**Input:** arr = \[100,100,100\]
**Output:** \[1,1,1\]
**Explanation**: Same elements share the same rank.

**Example 3:**

**Input:** arr = \[37,12,28,9,100,56,80,5,12\]
**Output:** \[5,3,4,2,8,6,7,1,3\]

**Constraints:**

*   `0 <= arr.length <= 105`
*   `-109 <= arr[i] <= 109`

\- Every time you are in a cell you will collect all the gold in that cell. - From your position, you can walk one step to the left, right, up, or down. - You can't visit the same cell more than once. - Never visit a cell with 0 gold. - You can start and stop collecting gold from any position in the grid that has some gold.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: getMaximumGold

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`.

**Summary:** Sort unique values, map value→rank, apply to original array. O(n log n) time. 

One flag: the TASK.md has conflicting info — it describes "rank-transform-of-an-array" but specifies `getMaximumGold` as the function name (a completely different problem). The correct LeetCode signature is `arrayRankTransform`. The implementer should use that.

[Committed changes to planner branch]