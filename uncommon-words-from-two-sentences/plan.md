# Plan (Iteration 1)

Task: Solve the LeetCode problem "uncommon-words-from-two-sentences":

A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

A word is **uncommon** if it appears exactly once in one of the sentences, and **does not appear** in the other sentence.

Given two **sentences** `s1` and `s2`, return _a list of all the **uncommon words**_. You may return the answer in **any order**.

**Example 1:**

**Input:** s1 = "this apple is sweet", s2 = "this apple is sour"
**Output:** \["sweet","sour"\]

**Example 2:**

**Input:** s1 = "apple apple", s2 = "banana"
**Output:** \["banana"\]

**Constraints:**

*   `1 <= s1.length, s2.length <= 200`
*   `s1` and `s2` consist of lowercase English letters and spaces.
*   `s1` and `s2` do not have leading or trailing spaces.
*   All the words in `s1` and `s2` are separated by a single space.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: k_similarity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is O(n) time/space using `Counter` on the concatenated word list — a word appearing exactly once total is by definition uncommon.

[Committed changes to planner branch]