# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-units-on-a-truck":

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

*   `numberOfBoxesi` is the number of boxes of type `i`.
*   `numberOfUnitsPerBoxi` is the number of units in each box of the type `i`.

You are also given an integer `truckSize`, which is the **maximum** number of **boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return _the **maximum** total number of **units** that can be put on the truck._

**Example 1:**

**Input:** boxTypes = \[\[1,3\],\[2,2\],\[3,1\]\], truckSize = 4
**Output:** 8
**Explanation:** There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 \* 3) + (2 \* 2) + (1 \* 1) = 8.

**Example 2:**

**Input:** boxTypes = \[\[5,10\],\[2,5\],\[4,7\],\[3,9\]\], truckSize = 10
**Output:** 91

**Constraints:**

*   `1 <= boxTypes.length <= 1000`
*   `1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000`
*   `1 <= truckSize <= 106`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: busiest_servers

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Greedy approach — sort box types by units-per-box descending, greedily fill the truck. O(n log n) time. One note: the required function name `busiest_servers` is clearly a template copy-paste error from a different problem, but I've followed the requirement as stated.

[Committed changes to planner branch]