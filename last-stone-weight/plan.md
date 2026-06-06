# Plan (Iteration 1)

Task: Solve the LeetCode problem "last-stone-weight":

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

*   If `x == y`, both stones are destroyed, and
*   If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return _the weight of the last remaining stone_. If there are no stones left, return `0`.

**Example 1:**

**Input:** stones = \[2,7,4,1,8,1\]
**Output:** 1
**Explanation:** 
We combine 7 and 8 to get 1 so the array converts to \[2,4,1,1,1\] then,
we combine 2 and 4 to get 2 so the array converts to \[2,1,1,1\] then,
we combine 2 and 1 to get 1 so the array converts to \[1,1,1\] then,
we combine 1 and 1 to get 0 so the array converts to \[1\] then that's the value of the last stone.

**Example 2:**

**Input:** stones = \[1\]
**Output:** 1

**Constraints:**

*   `1 <= stones.length <= 30`
*   `1 <= stones[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: longestOnes

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is a standard max-heap solution — negate values for Python's min-heap, repeatedly pop the two largest, push back the difference if non-zero. The `longestOnes` function name in the task is a copy-paste error; the correct LeetCode signature is `lastStoneWeight`.

[Committed changes to planner branch]