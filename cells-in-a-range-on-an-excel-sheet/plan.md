# Plan (Iteration 1)

Task: Solve the LeetCode problem "cells-in-a-range-on-an-excel-sheet":

A cell `(r, c)` of an excel sheet is represented as a string `" "` where:

*   denotes the column number `c` of the cell. It is represented by **alphabetical letters**.
    *   For example, the `1st` column is denoted by `'A'`, the `2nd` by `'B'`, the `3rd` by `'C'`, and so on.
*   is the row number `r` of the cell. The `rth` row is represented by the **integer** `r`.

You are given a string `s` in the format `": "`, where represents the column `c1`, represents the row `r1`, represents the column `c2`, and represents the row `r2`, such that `r1 <= r2` and `c1 <= c2`.

Return _the **list of cells**_ `(x, y)` _such that_ `r1 <= x <= r2` _and_ `c1 <= y <= c2`. The cells should be represented as **strings** in the format mentioned above and be sorted in **non-decreasing** order first by columns and then by rows.

**Example 1:**

**Input:** s =  "K1:L2 "
**Output:** \[ "K1 ", "K2 ", "L1 ", "L2 "\]
**Explanation:**
The above diagram shows the cells which should be present in the list.
The red arrows denote the order in which the cells should be presented.

**Example 2:**

**Input:** s =  "A1:F1 "
**Output:** \[ "A1 ", "B1 ", "C1 ", "D1 ", "E1 ", "F1 "\]
**Explanation:**
The above diagram shows the cells which should be present in the list.
The red arrow denotes the order in which the cells should be presented.

**Constraints:**

*   `s.length == 5`
*   `'A' <= s[0] <= s[3] <= 'Z'`
*   `'1' <= s[1] <= s[4] <= '9'`
*   `s` consists of uppercase English letters, digits and `':'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: cell_range

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The problem is simple enough that there's really only one sensible approach — nested loops over the column and row ranges, which naturally produces the required ordering.

[Committed changes to planner branch]