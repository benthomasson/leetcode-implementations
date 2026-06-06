# Plan (Iteration 1)

Task: Solve the LeetCode problem "sum-of-left-leaves":

Given the `root` of a binary tree, return _the sum of all left leaves._

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

**Example 1:**

**Input:** root = \[3,9,20,null,null,15,7\]
**Output:** 24
**Explanation:** There are two left leaves in the binary tree, with values 9 and 15 respectively.

**Example 2:**

**Input:** root = \[1\]
**Output:** 0

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 1000]`.
*   `-1000 <= Node.val <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sum_of_left_leaves

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Recursive DFS, check if left child is a leaf, sum values. Straightforward.

[Committed changes to planner branch]