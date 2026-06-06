# Plan (Iteration 1)

Task: Solve the LeetCode problem "palindrome-linked-list":

Given the `head` of a singly linked list, return `true` _if it is a_ _palindrome_ _or_ `false` _otherwise_.

**Example 1:**

**Input:** head = \[1,2,2,1\]
**Output:** true

**Example 2:**

**Input:** head = \[1,2\]
**Output:** false

**Constraints:**

*   The number of nodes in the list is in the range `[1, 105]`.
*   `0 <= Node.val <= 9`

**Follow up:** Could you do it in `O(n)` time and `O(1)` space?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: isPalindrome

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Summary: reverse-second-half approach, O(n) time, O(1) space — the standard optimal solution. Confidence: **HIGH**.

[Committed changes to planner branch]