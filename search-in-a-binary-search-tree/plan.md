# Plan (Iteration 1)

Task: Solve the LeetCode problem "search-in-a-binary-search-tree":

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Example 1:**

**Input:** root = \[4,2,7,1,3\], val = 2
**Output:** \[2,1,3\]

**Example 2:**

**Input:** root = \[4,2,7,1,3\], val = 5
**Output:** \[\]

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 5000]`.
*   `1 <= Node.val <= 107`
*   `root` is a binary search tree.
*   `1 <= val <= 107`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: searchBST

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a textbook BST lookup — iterative traversal is the clear optimal choice.

[Committed changes to planner branch]