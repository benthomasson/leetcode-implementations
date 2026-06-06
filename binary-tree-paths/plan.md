# Plan (Iteration 1)

Task: Solve the LeetCode problem "binary-tree-paths":

Given the `root` of a binary tree, return _all root-to-leaf paths in **any order**_.

A **leaf** is a node with no children.

**Example 1:**

**Input:** root = \[1,2,3,null,5\]
**Output:** \[ "1->2->5 ", "1->3 "\]

**Example 2:**

**Input:** root = \[1\]
**Output:** \[ "1 "\]

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 100]`.
*   `-100 <= Node.val <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: binary_tree_paths

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Recursive DFS, straightforward implementation — ready for the implementer.

[Committed changes to planner branch]