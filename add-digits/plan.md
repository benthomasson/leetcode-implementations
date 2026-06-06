# Plan (Iteration 1)

Task: Solve the LeetCode problem "add-digits":

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

**Example 1:**

**Input:** num = 38
**Output:** 2
**Explanation:** The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

**Example 2:**

**Input:** num = 0
**Output:** 0

**Constraints:**

*   `0 <= num <= 231 - 1`

**Follow up:** Could you do it without any loop/recursion in `O(1)` runtime?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: addDigits

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The digital root formula `1 + (num - 1) % 9` (with special case for 0) gives an optimal O(1) solution. Tests should cover zero, single digits, the example case (38→2), multiples of 9, and large values.

[Committed changes to planner branch]