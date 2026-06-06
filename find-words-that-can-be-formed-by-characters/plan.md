# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-words-that-can-be-formed-by-characters":

You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from chars (each character can only be used once).

Return _the sum of lengths of all good strings in words_.

**Example 1:**

**Input:** words = \[ "cat ", "bt ", "hat ", "tree "\], chars =  "atach "
**Output:** 6
**Explanation:** The strings that can be formed are  "cat " and  "hat " so the answer is 3 + 3 = 6.

**Example 2:**

**Input:** words = \[ "hello ", "world ", "leetcode "\], chars =  "welldonehoneyr "
**Output:** 10
**Explanation:** The strings that can be formed are  "hello " and  "world " so the answer is 5 + 5 = 10.

**Constraints:**

*   `1 <= words.length <= 1000`
*   `1 <= words[i].length, chars.length <= 100`
*   `words[i]` and `chars` consist of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: num_tile_possibilities

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is straightforward: Counter-based character frequency comparison, O(n·m) time, O(1) space.

[Committed changes to planner branch]