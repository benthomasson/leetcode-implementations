# Plan (Iteration 1)

Task: Solve the LeetCode problem "largest-triangle-area":

Given an array of points on the **X-Y** plane `points` where `points[i] = [xi, yi]`, return _the area of the largest triangle that can be formed by any three different points_. Answers within `10-5` of the actual answer will be accepted.

**Example 1:**

**Input:** points = \[\[0,0\],\[0,1\],\[1,0\],\[0,2\],\[2,0\]\]
**Output:** 2.00000
**Explanation:** The five points are shown in the above figure. The red triangle is the largest.

**Example 2:**

**Input:** points = \[\[1,0\],\[0,0\],\[0,1\]\]
**Output:** 0.50000

**Constraints:**

*   `3 <= points.length <= 50`
*   `-50 <= xi, yi <= 50`
*   All the given points are **unique**.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_shifted

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is straightforward: Shoelace formula over all triples, O(n³) which is perfectly fine for n≤50.

[Committed changes to planner branch]