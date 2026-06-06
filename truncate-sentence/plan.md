# Plan (Iteration 1)

Task: Solve the LeetCode problem "truncate-sentence":

A **sentence** is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of **only** uppercase and lowercase English letters (no punctuation).

*   For example, `"Hello World "`, `"HELLO "`, and `"hello world hello world "` are all sentences.

You are given a sentence `s`​​​​​​ and an integer `k`​​​​​​. You want to **truncate** `s`​​​​​​ such that it contains only the **first** `k`​​​​​​ words. Return `s`​​​​_​​ after **truncating** it._

**Example 1:**

**Input:** s =  "Hello how are you Contestant ", k = 4
**Output:**  "Hello how are you "
**Explanation:**
The words in s are \[ "Hello ",  "how "  "are ",  "you ",  "Contestant "\].
The first 4 words are \[ "Hello ",  "how ",  "are ",  "you "\].
Hence, you should return  "Hello how are you ".

**Example 2:**

**Input:** s =  "What is the solution to this problem ", k = 4
**Output:**  "What is the solution "
**Explanation:**
The words in s are \[ "What ",  "is "  "the ",  "solution ",  "to ",  "this ",  "problem "\].
The first 4 words are \[ "What ",  "is ",  "the ",  "solution "\].
Hence, you should return  "What is the solution ".

**Example 3:**

**Input:** s =  "chopper is not a tanuki ", k = 5
**Output:**  "chopper is not a tanuki "

**Constraints:**

*   `1 <= s.length <= 500`
*   `k` is in the range `[1, the number of words in s]`.
*   `s` consist of only lowercase and uppercase English letters and spaces.
*   The words in `s` are separated by a single space.
*   There are no leading or trailing spaces.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: truncateSentence

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is a one-liner: `' '.join(s.split()[:k])`. The implementer just needs to wrap it with proper docstring, type hints, and tests.

[Committed changes to planner branch]