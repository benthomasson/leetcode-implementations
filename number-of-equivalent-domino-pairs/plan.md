# Plan (Iteration 1)

Task: Solve the LeetCode problem "number-of-equivalent-domino-pairs":

Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`) - that is, one domino can be rotated to be equal to another domino.

Return _the number of pairs_ `(i, j)` _for which_ `0 <= i < j < dominoes.length`_, and_ `dominoes[i]` _is **equivalent to**_ `dominoes[j]`.

**Example 1:**

**Input:** dominoes = \[\[1,2\],\[2,1\],\[3,4\],\[5,6\]\]
**Output:** 1

**Example 2:**

**Input:** dominoes = \[\[1,2\],\[1,2\],\[1,1\],\[1,2\],\[2,2\]\]
**Output:** 3

**Constraints:**

*   `1 <= dominoes.length <= 4 * 104`
*   `dominoes[i].length == 2`
*   `1 <= dominoes[i][j] <= 9`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: remove_duplicates

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. 

**Summary:** Normalize each domino to `(min, max)`, count with a hash map, compute pairs as `n*(n-1)//2` per group. O(n) time. Tests should cover both examples, edge cases (single domino, all same, palindromes like `[1,1]`), and the max constraint.

[Committed changes to planner branch]