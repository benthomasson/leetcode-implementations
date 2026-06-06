# Plan (Iteration 1)

Task: Solve the LeetCode problem "check-if-it-is-a-straight-line":

You are given an array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.

**Example 1:**

**Input:** coordinates = \[\[1,2\],\[2,3\],\[3,4\],\[4,5\],\[5,6\],\[6,7\]\]
**Output:** true

**Example 2:**

**Input:** coordinates = \[\[1,1\],\[2,2\],\[3,4\],\[4,5\],\[5,6\],\[7,7\]\]
**Output:** false

**Constraints:**

*   `2 <= coordinates.length <= 1000`
*   `coordinates[i].length == 2`
*   `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4`
*   `coordinates` contains no duplicate point.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: findBestValue

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `/workspaces/check-if-it-is-a-straight-line/PLAN.md`.

**Summary:** Use cross-product collinearity check — O(n) time, O(1) space. For each point after the first two, verify `(x - x0) * dy - (y - y0) * dx == 0`. This naturally handles vertical and horizontal lines without special cases. Function named `findBestValue` per requirements. Tests should cover the two examples, 2-point input, vertical/horizontal lines, and negative coordinates.