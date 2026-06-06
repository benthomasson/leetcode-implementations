# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-population-year":

You are given a 2D integer array `logs` where each `logs[i] = [birthi, deathi]` indicates the birth and death years of the `ith` person.

The **population** of some year `x` is the number of people alive during that year. The `ith` person is counted in year `x`'s population if `x` is in the **inclusive** range `[birthi, deathi - 1]`. Note that the person is **not** counted in the year that they die.

Return _the **earliest** year with the **maximum population**_.

**Example 1:**

**Input:** logs = \[\[1993,1999\],\[2000,2010\]\]
**Output:** 1993
**Explanation:** The maximum population is 1, and 1993 is the earliest year with this population.

**Example 2:**

**Input:** logs = \[\[1950,1961\],\[1960,1971\],\[1970,1981\]\]
**Output:** 1960
**Explanation:** 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

**Constraints:**

*   `1 <= logs.length <= 100`
*   `1950 <= birthi < deathi <= 2050`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maxAliveYear

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is a standard difference array / line sweep — simple, optimal, and well-suited for the constrained year range.

[Committed changes to planner branch]