# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-cuts-to-divide-a-circle":

A **valid cut** in a circle can be:

*   A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or
*   A cut that is represented by a straight line that touches one point on the edge of the circle and its center.

Some valid and invalid cuts are shown in the figures below.

Given the integer `n`, return _the **minimum** number of cuts needed to divide a circle into_ `n` _equal slices_.

**Example 1:**

**Input:** n = 4
**Output:** 2
**Explanation:** 
The above figure shows how cutting the circle twice through the middle divides it into 4 equal slices.

**Example 2:**

**Input:** n = 3
**Output:** 3
**Explanation:**
At least 3 cuts are needed to divide the circle into 3 equal slices. 
It can be shown that less than 3 cuts cannot result in 3 slices of equal size and shape.
Also note that the first cut will not divide the circle into distinct parts.

**Constraints:**

*   `1 <= n <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: min_cuts

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is a simple three-case conditional — no complex algorithm needed.

[Committed changes to planner branch]