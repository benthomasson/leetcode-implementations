# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-mode-in-binary-search-tree":

Given the `root` of a binary search tree (BST) with duplicates, return _all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (i.e., the most frequently occurred element) in it_.

If the tree has more than one mode, return them in **any order**.

Assume a BST is defined as follows:

*   The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
*   The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
*   Both the left and right subtrees must also be binary search trees.

**Example 1:**

**Input:** root = \[1,null,2,2\]
**Output:** \[2\]

**Example 2:**

**Input:** root = \[0\]
**Output:** \[0\]

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 104]`.
*   `-105 <= Node.val <= 105`

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: findMode

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is straightforward: leverage BST's sorted in-order traversal to count consecutive equal values, tracking the max frequency as you go. O(n) time, O(1) extra space.

[Committed changes to planner branch]