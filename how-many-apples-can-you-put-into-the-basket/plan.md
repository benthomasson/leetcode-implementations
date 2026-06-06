# Plan (Iteration 1)

Task: Solve the LeetCode problem "how-many-apples-can-you-put-into-the-basket":

You have some apples and a basket that can carry up to `5000` units of weight.

Given an integer array `weight` where `weight[i]` is the weight of the `ith` apple, return _the maximum number of apples you can put in the basket_.

**Example 1:**

**Input:** weight = \[100,200,150,1000\]
**Output:** 4
**Explanation:** All 4 apples can be carried by the basket since their sum of weights is 1450.

**Example 2:**

**Input:** weight = \[900,950,800,1000,700,800\]
**Output:** 5
**Explanation:** The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.

**Constraints:**

*   `1 <= weight.length <= 103`
*   `1 <= weight[i] <= 103`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: minHeightShelves

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Sort ascending, greedily take lightest apples until weight cap (5000) is hit. Note the function name in the task (`minHeightShelves`) is incorrect — it should be `maxNumberOfApples` per the actual LeetCode problem.

[Committed changes to planner branch]