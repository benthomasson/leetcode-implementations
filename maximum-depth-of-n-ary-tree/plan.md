# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-depth-of-n-ary-tree":

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

_Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples)._

**Example 1:**

**Input:** root = \[1,null,3,2,4,null,5,6\]
**Output:** 3

**Example 2:**

**Input:** root = \[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14\]
**Output:** 5

**Constraints:**

*   The total number of nodes is in the range `[0, 104]`.
*   The depth of the n-ary tree is less than or equal to `1000`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_depth

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Recursive DFS is the clear choice here — simple, optimal, and well within constraints.

[Committed changes to planner branch]