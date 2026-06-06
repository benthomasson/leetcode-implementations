# Plan (Iteration 1)

Task: Solve the LeetCode problem "binary-gap":

Given a positive integer `n`, find and return _the **longest distance** between any two **adjacent**_ `1`_'s in the binary representation of_ `n`_. If there are no two adjacent_ `1`_'s, return_ `0`_._

Two `1`'s are **adjacent** if there are only `0`'s separating them (possibly no `0`'s). The **distance** between two `1`'s is the absolute difference between their bit positions. For example, the two `1`'s in `"1001 "` have a distance of 3.

**Example 1:**

**Input:** n = 22
**Output:** 2
**Explanation:** 22 in binary is  "10110 ".
The first adjacent pair of 1's is  "10110 " with a distance of 2.
The second adjacent pair of 1's is  "10110 " with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that  "10110 " is not a valid pair since there is a 1 separating the two 1's underlined.

**Example 2:**

**Input:** n = 8
**Output:** 0
**Explanation:** 8 in binary is  "1000 ".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

**Example 3:**

**Input:** n = 5
**Output:** 2
**Explanation:** 5 in binary is  "101 ".

**Constraints:**

*   `1 <= n <= 109`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: push_dominoes

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward bit-shifting solution — iterate bits, track positions of 1-bits, compute max gap. O(log n) time, O(1) space.

[Committed changes to planner branch]