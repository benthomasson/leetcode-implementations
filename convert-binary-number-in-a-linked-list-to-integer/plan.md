# Plan (Iteration 1)

Task: Solve the LeetCode problem "convert-binary-number-in-a-linked-list-to-integer":

Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either `0` or `1`. The linked list holds the binary representation of a number.

Return the _decimal value_ of the number in the linked list.

The **most significant bit** is at the head of the linked list.

**Example 1:**

**Input:** head = \[1,0,1\]
**Output:** 5
**Explanation:** (101) in base 2 = (5) in base 10

**Example 2:**

**Input:** head = \[0\]
**Output:** 0

**Constraints:**

*   The Linked List is not empty.
*   Number of nodes will not exceed `30`.
*   Each node's value is either `0` or `1`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: min_operations

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The problem is straightforward — single-pass bit-shift accumulation, O(n) time, O(1) space.

[Committed changes to planner branch]