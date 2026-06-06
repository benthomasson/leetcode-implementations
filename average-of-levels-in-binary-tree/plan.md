# Plan (Iteration 1)

Task: Solve the LeetCode problem "average-of-levels-in-binary-tree":

Given the `root` of a binary tree, return _the average value of the nodes on each level in the form of an array_. Answers within `10-5` of the actual answer will be accepted.

**Example 1:**

**Input:** root = \[3,9,20,null,null,15,7\]
**Output:** \[3.00000,14.50000,11.00000\]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return \[3, 14.5, 11\].

**Example 2:**

**Input:** root = \[3,9,20,15,7\]
**Output:** \[3.00000,14.50000,11.00000\]

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 104]`.
*   `-231 <= Node.val <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: averageOfLevels

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. BFS level-order traversal is the clear choice here — simple, optimal, and directly maps to the problem structure.

[Committed changes to planner branch]