# Plan (Iteration 1)

Task: Solve the LeetCode problem "reverse-linked-list":

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

**Example 1:**

**Input:** head = \[1,2,3,4,5\]
**Output:** \[5,4,3,2,1\]

**Example 2:**

**Input:** head = \[1,2\]
**Output:** \[2,1\]

**Example 3:**

**Input:** head = \[\]
**Output:** \[\]

**Constraints:**

*   The number of nodes in the list is the range `[0, 5000]`.
*   `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: reverse_list

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a textbook problem — the iterative three-pointer swap is the optimal approach. The implementer should have no trouble with this one.

[Committed changes to planner branch]