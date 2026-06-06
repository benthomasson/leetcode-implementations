# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-enemy-forts-that-can-be-captured":

You are given a **0-indexed** integer array `forts` of length `n` representing the positions of several forts. `forts[i]` can be `-1`, `0`, or `1` where:

*   `-1` represents there is **no fort** at the `ith` position.
*   `0` indicates there is an **enemy** fort at the `ith` position.
*   `1` indicates the fort at the `ith` the position is under your command.

Now you have decided to move your army from one of your forts at position `i` to an empty position `j` such that:

*   `0 <= i, j <= n - 1`
*   The army travels over enemy forts **only**. Formally, for all `k` where `min(i,j) < k < max(i,j)`, `forts[k] == 0.`

While moving the army, all the enemy forts that come in the way are **captured**.

Return _the **maximum** number of enemy forts that can be captured_. In case it is **impossible** to move your army, or you do not have any fort under your command, return `0`_._

**Example 1:**

**Input:** forts = \[1,0,0,-1,0,0,0,0,1\]
**Output:** 4
**Explanation:**
- Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
- Moving the army from position 8 to position 3 captures 4 enemy forts.
Since 4 is the maximum number of enemy forts that can be captured, we return 4.

**Example 2:**

**Input:** forts = \[0,0,1,-1\]
**Output:** 0
**Explanation:** Since no enemy fort can be captured, 0 is returned.

**Constraints:**

*   `1 <= forts.length <= 1000`
*   `-1 <= forts[i] <= 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_captured_forts

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is a simple O(n) linear scan — track the last non-zero index and when you find a new non-zero value of the opposite sign, the distance minus one gives the captured forts count.

[Committed changes to planner branch]