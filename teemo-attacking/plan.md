# Plan (Iteration 1)

Task: Solve the LeetCode problem "teemo-attacking":

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly `duration` seconds. More formally, an attack at second `t` will mean Ashe is poisoned during the **inclusive** time interval `[t, t + duration - 1]`. If Teemo attacks again **before** the poison effect ends, the timer for it is **reset**, and the poison effect will end `duration` seconds after the new attack.

You are given a **non-decreasing** integer array `timeSeries`, where `timeSeries[i]` denotes that Teemo attacks Ashe at second `timeSeries[i]`, and an integer `duration`.

Return _the **total** number of seconds that Ashe is poisoned_.

**Example 1:**

**Input:** timeSeries = \[1,4\], duration = 2
**Output:** 4
**Explanation:** Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

**Example 2:**

**Input:** timeSeries = \[1,2\], duration = 2
**Output:** 3
**Explanation:** Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

**Constraints:**

*   `1 <= timeSeries.length <= 104`
*   `0 <= timeSeries[i], duration <= 107`
*   `timeSeries` is sorted in **non-decreasing** order.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: find_poisoned_duration

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The algorithm is a simple linear scan — for each pair of consecutive attacks, contribute `min(timeSeries[i+1] - timeSeries[i], duration)`, then add `duration` for the last attack. O(n) time, O(1) space.

[Committed changes to planner branch]