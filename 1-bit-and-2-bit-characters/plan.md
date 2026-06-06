# Plan (Iteration 1)

Task: Solve the LeetCode problem "1-bit-and-2-bit-characters":

We have two special characters:

*   The first character can be represented by one bit `0`.
*   The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

**Example 1:**

**Input:** bits = \[1,0,0\]
**Output:** true
**Explanation:** The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

**Example 2:**

**Input:** bits = \[1,1,1,0\]
**Output:** false
**Explanation:** The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

**Constraints:**

*   `1 <= bits.length <= 1000`
*   `bits[i]` is either `0` or `1`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_one_bit_character

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The greedy scan approach is optimal and unambiguous for this problem.

[Committed changes to planner branch]