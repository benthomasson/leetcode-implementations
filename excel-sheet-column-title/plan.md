# Plan (Iteration 1)

Task: Solve the LeetCode problem "excel-sheet-column-title":

Given an integer `columnNumber`, return _its corresponding column title as it appears in an Excel sheet_.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

**Example 1:**

**Input:** columnNumber = 1
**Output:**  "A "

**Example 2:**

**Input:** columnNumber = 28
**Output:**  "AB "

**Example 3:**

**Input:** columnNumber = 701
**Output:**  "ZY "

**Constraints:**

*   `1 <= columnNumber <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: convert_to_title

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The problem is a classic 1-indexed base-26 conversion — subtract 1 each iteration to handle the offset, then standard digit extraction.

[Committed changes to planner branch]