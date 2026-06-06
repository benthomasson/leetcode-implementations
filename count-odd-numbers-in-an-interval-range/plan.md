# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-odd-numbers-in-an-interval-range":

Given two non-negative integers `low` and `high`. Return the _count of odd numbers between_ `low` _and_ `high` _(inclusive)_.

**Example 1:**

**Input:** low = 3, high = 7
**Output:** 3
**Explanation:** The odd numbers between 3 and 7 are \[3,5,7\].

**Example 2:**

**Input:** low = 8, high = 10
**Output:** 1
**Explanation:** The odd numbers between 8 and 10 are \[9\].

**Constraints:**

*   `0 <= low <= high <= 10^9`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_odds

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is using integer division to count odds mathematically in O(1) rather than iterating — critical given constraints up to 10^9.

[Committed changes to planner branch]