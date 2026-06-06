# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-center-of-star-graph":

There is an undirected **star** graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one **center** node and **exactly** `n - 1` edges that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [ui, vi]` indicates that there is an edge between the nodes `ui` and `vi`. Return the center of the given star graph.

**Example 1:**

**Input:** edges = \[\[1,2\],\[2,3\],\[4,2\]\]
**Output:** 2
**Explanation:** As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

**Example 2:**

**Input:** edges = \[\[1,2\],\[5,1\],\[1,3\],\[1,4\]\]
**Output:** 1

**Constraints:**

*   `3 <= n <= 105`
*   `edges.length == n - 1`
*   `edges[i].length == 2`
*   `1 <= ui, vi <= n`
*   `ui != vi`
*   The given `edges` represent a valid star graph.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maximum_wealth

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight: since every edge connects to the center in a star graph, just find the common node between the first two edges — O(1) time and space.

[Committed changes to planner branch]