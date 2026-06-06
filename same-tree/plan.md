# Plan (Iteration 1)

Task: Solve the LeetCode problem "same-tree":

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**

**Input:** p = \[1,2,3\], q = \[1,2,3\]
**Output:** true

**Example 2:**

**Input:** p = \[1,2\], q = \[1,null,2\]
**Output:** false

**Example 3:**

**Input:** p = \[1,2,1\], q = \[1,1,2\]
**Output:** false

**Constraints:**

*   The number of nodes in both trees is in the range `[0, 100]`.
*   `-104 <= Node.val <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_same_tree

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple recursive DFS — compare nodes pairwise, recurse on children. Nothing exotic needed here.

[Committed changes to planner branch]