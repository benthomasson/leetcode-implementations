# Plan (Iteration 1)

Task: Solve the LeetCode problem "final-value-of-variable-after-performing-operations":

There is a programming language with only **four** operations and **one** variable `X`:

*   `++X` and `X++` **increments** the value of the variable `X` by `1`.
*   `--X` and `X--` **decrements** the value of the variable `X` by `1`.

Initially, the value of `X` is `0`.

Given an array of strings `operations` containing a list of operations, return _the **final** value of_ `X` _after performing all the operations_.

**Example 1:**

**Input:** operations = \[ "--X ", "X++ ", "X++ "\]
**Output:** 1
**Explanation:** The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.

**Example 2:**

**Input:** operations = \[ "++X ", "++X ", "X++ "\]
**Output:** 3
**Explanation:** The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.

**Example 3:**

**Input:** operations = \[ "X++ ", "++X ", "--X ", "X-- "\]
**Output:** 0
**Explanation:** The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.

**Constraints:**

*   `1 <= operations.length <= 100`
*   `operations[i]` will be either `"++X "`, `"X++ "`, `"--X "`, or `"X-- "`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_value

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: check the middle character of each operation string to determine increment vs decrement, accumulate, and return. High confidence — this is a straightforward problem.

[Committed changes to planner branch]