# Plan (Iteration 1)

Task: Solve the LeetCode problem "the-k-weakest-rows-in-a-matrix":

You are given an `m x n` binary matrix `mat` of `1`'s (representing soldiers) and `0`'s (representing civilians). The soldiers are positioned **in front** of the civilians. That is, all the `1`'s will appear to the **left** of all the `0`'s in each row.

A row `i` is **weaker** than a row `j` if one of the following is true:

*   The number of soldiers in row `i` is less than the number of soldiers in row `j`.
*   Both rows have the same number of soldiers and `i < j`.

Return _the indices of the_ `k` _**weakest** rows in the matrix ordered from weakest to strongest_.

**Example 1:**

**Input:** mat = 
\[\[1,1,0,0,0\],
 \[1,1,1,1,0\],
 \[1,0,0,0,0\],
 \[1,1,0,0,0\],
 \[1,1,1,1,1\]\], 
k = 3
**Output:** \[2,0,3\]
**Explanation:** 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are \[2,0,3,1,4\].

**Example 2:**

**Input:** mat = 
\[\[1,0,0,0\],
 \[1,1,1,1\],
 \[1,0,0,0\],
 \[1,0,0,0\]\], 
k = 2
**Output:** \[0,2\]
**Explanation:** 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are \[0,2,3,1\].

**Constraints:**

*   `m == mat.length`
*   `n == mat[i].length`
*   `2 <= n, m <= 100`
*   `1 <= k <= m`
*   `matrix[i][j]` is either 0 or 1.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: kWeakestRows

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

## PLAN

**Algorithm:** Count soldiers per row with `sum()`, pair with row index, sort by `(count, index)`, return first `k` indices. Tie-breaking is automatic. O(m·n + m·log m) time, O(m) space.

**Implementation:** Two files — `solution.py` with typed, documented function; `tests/test_solution.py` covering both examples plus edge cases (all 1s, all 0s, k=m, single row, 2×2 minimum).

## SELF-REVIEW

1. **What went well:** Clear problem with an obvious optimal approach — no ambiguity in requirements.
2. **Missing info:** None needed; problem is self-contained.
3. **Next time:** Nothing to improve for problems this straightforward.
4. **Confidence: HIGH** — Textbook sorting problem, constraints are tiny, no tricky edge cases.

[Committed changes to planner branch]