# Plan (Iteration 1)

Task: Solve the LeetCode problem "excel-sheet-column-number":

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return _its corresponding column number_.

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

**Input:** columnTitle =  "A "
**Output:** 1

**Example 2:**

**Input:** columnTitle =  "AB "
**Output:** 28

**Example 3:**

**Input:** columnTitle =  "ZY "
**Output:** 701

**Constraints:**

*   `1 <= columnTitle.length <= 7`
*   `columnTitle` consists only of uppercase English letters.
*   `columnTitle` is in the range `[ "A ", "FXSHRXW "]`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: title_to_number

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The algorithm is a simple left-to-right base-26 accumulation — no design decisions needed beyond that.

[Committed changes to planner branch]