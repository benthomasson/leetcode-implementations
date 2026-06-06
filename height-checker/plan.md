# Plan (Iteration 1)

Task: Solve the LeetCode problem "height-checker":

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the `ith` student in line (**0-indexed**).

Return _the **number of indices** where_ `heights[i] != expected[i]`.

**Example 1:**

**Input:** heights = \[1,1,4,2,1,3\]
**Output:** 3
**Explanation:** 
heights:  \[1,1,4,2,1,3\]
expected: \[1,1,1,2,3,4\]
Indices 2, 4, and 5 do not match.

**Example 2:**

**Input:** heights = \[5,1,2,3,4\]
**Output:** 5
**Explanation:**
heights:  \[5,1,2,3,4\]
expected: \[1,2,3,4,5\]
All indices do not match.

**Example 3:**

**Input:** heights = \[1,2,3,4,5\]
**Output:** 0
**Explanation:**
heights:  \[1,2,3,4,5\]
expected: \[1,2,3,4,5\]
All indices match.

**Constraints:**

*   `1 <= heights.length <= 100`
*   `1 <= heights[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: height_checker

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is using counting sort to get O(n) time given the bounded height range [1, 100].

[Committed changes to planner branch]