# Plan (Iteration 1)

Task: Solve the LeetCode problem "merge-two-binary-trees":

You are given two binary trees `root1` and `root2`.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return _the merged tree_.

**Note:** The merging process must start from the root nodes of both trees.

**Example 1:**

**Input:** root1 = \[1,3,2,5\], root2 = \[2,1,3,null,4,null,7\]
**Output:** \[3,4,5,5,4,null,7\]

**Example 2:**

**Input:** root1 = \[1\], root2 = \[1,2\]
**Output:** \[2,2\]

**Constraints:**

*   The number of nodes in both trees is in the range `[0, 2000]`.
*   `-104 <= Node.val <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: merge_trees

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple recursive DFS — sum overlapping nodes, pass through non-overlapping subtrees, O(min(n,m)) complexity.

[Committed changes to planner branch]