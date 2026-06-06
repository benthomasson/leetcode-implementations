# Plan (Iteration 1)

Task: Solve the LeetCode problem "k-items-with-the-maximum-sum":

There is a bag that consists of items, each item has a number `1`, `0`, or `-1` written on it.

You are given four **non-negative** integers `numOnes`, `numZeros`, `numNegOnes`, and `k`.

The bag initially contains:

*   `numOnes` items with `1`s written on them.
*   `numZeroes` items with `0`s written on them.
*   `numNegOnes` items with `-1`s written on them.

We want to pick exactly `k` items among the available items. Return _the **maximum** possible sum of numbers written on the items_.

**Example 1:**

**Input:** numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
**Output:** 2
**Explanation:** We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
It can be proven that 2 is the maximum possible sum.

**Example 2:**

**Input:** numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
**Output:** 3
**Explanation:** We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
It can be proven that 3 is the maximum possible sum.

**Constraints:**

*   `0 <= numOnes, numZeros, numNegOnes <= 50`
*   `0 <= k <= numOnes + numZeros + numNegOnes`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_sum

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is that this is a simple greedy problem with an O(1) closed-form solution: `min(k, numOnes) - max(0, k - numOnes - numZeros)`.

[Committed changes to planner branch]