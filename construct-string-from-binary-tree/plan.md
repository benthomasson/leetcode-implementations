# Plan (Iteration 1)

Task: Solve the LeetCode problem "construct-string-from-binary-tree":

Given the `root` of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

**Example 1:**

**Input:** root = \[1,2,3,4\]
**Output:**  "1(2(4))(3) "
**Explanation:** Originally, it needs to be  "1(2(4)())(3()()) ", but you need to omit all the unnecessary empty parenthesis pairs. And it will be  "1(2(4))(3) "

**Example 2:**

**Input:** root = \[1,2,3,null,4\]
**Output:**  "1(2()(4))(3) "
**Explanation:** Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 104]`.
*   `-1000 <= Node.val <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: tree2str

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Use recursive preorder DFS. For each node, stringify its value, then append `(left)` and `(right)` with the key rule: omit right `()` if right is null, but keep left `()` if left is null and right exists. O(n) time and space. High confidence — straightforward tree recursion.

[Committed changes to planner branch]