# Plan (Iteration 1)

Task: Solve the LeetCode problem "single-row-keyboard":

There is a special keyboard with **all keys in a single row**.

Given a string `keyboard` of length `26` indicating the layout of the keyboard (indexed from `0` to `25`). Initially, your finger is at index `0`. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index `i` to index `j` is `|i - j|`.

You want to type a string `word`. Write a function to calculate how much time it takes to type it with one finger.

**Example 1:**

**Input:** keyboard =  "abcdefghijklmnopqrstuvwxyz ", word =  "cba "
**Output:** 4
**Explanation:** The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 

**Example 2:**

**Input:** keyboard =  "pqrstuvwxyzabcdefghijklmno ", word =  "leetcode "
**Output:** 73

**Constraints:**

*   `keyboard.length == 26`
*   `keyboard` contains each English lowercase letter exactly once in some order.
*   `1 <= word.length <= 104`
*   `word[i]` is an English lowercase letter.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: calculate_time

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The problem is straightforward — hash map for O(1) lookups, single pass through the word. Ready for implementation.

[Committed changes to planner branch]