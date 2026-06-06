# Plan (Iteration 1)

Task: Solve the LeetCode problem "distribute-money-to-maximum-children":

You are given an integer `money` denoting the amount of money (in dollars) that you have and another integer `children` denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

*   All money must be distributed.
*   Everyone must receive at least `1` dollar.
*   Nobody receives `4` dollars.

Return _the **maximum** number of children who may receive **exactly**_ `8` _dollars if you distribute the money according to the aforementioned rules_. If there is no way to distribute the money, return `-1`.

**Example 1:**

**Input:** money = 20, children = 3
**Output:** 1
**Explanation:** 
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.

**Example 2:**

**Input:** money = 16, children = 2
**Output:** 2
**Explanation:** Each child can be given 8 dollars.

**Constraints:**

*   `1 <= money <= 200`
*   `2 <= children <= 30`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maximum_children_with_eight_dollars

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Greedy O(1) approach — give everyone $1, then greedily upgrade children to $8 by adding $7 more. Three edge cases to handle: impossible distribution, surplus when all children hit $8, and avoiding the $4 amount on the last remaining child.

[Committed changes to planner branch]