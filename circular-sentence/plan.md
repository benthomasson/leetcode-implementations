# Plan (Iteration 1)

Task: Solve the LeetCode problem "circular-sentence":

A **sentence** is a list of words that are separated by a **single** space with no leading or trailing spaces.

*   For example, `"Hello World "`, `"HELLO "`, `"hello world hello world "` are all sentences.

Words consist of **only** uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is **circular** if:

*   The last character of a word is equal to the first character of the next word.
*   The last character of the last word is equal to the first character of the first word.

For example, `"leetcode exercises sound delightful "`, `"eetcode "`, `"leetcode eats soul "` are all circular sentences. However, `"Leetcode is cool "`, `"happy Leetcode "`, `"Leetcode "` and `"I like Leetcode "` are **not** circular sentences.

Given a string `sentence`, return `true` _if it is circular_. Otherwise, return `false`.

**Example 1:**

**Input:** sentence =  "leetcode exercises sound delightful "
**Output:** true
**Explanation:** The words in sentence are \[ "leetcode ",  "exercises ",  "sound ",  "delightful "\].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

**Example 2:**

**Input:** sentence =  "eetcode "
**Output:** true
**Explanation:** The words in sentence are \[ "eetcode "\].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.

**Example 3:**

**Input:** sentence =  "Leetcode is cool "
**Output:** false
**Explanation:** The words in sentence are \[ "Leetcode ",  "is ",  "cool "\].
- Leetcode's last character is **not** equal to is's first character.
The sentence is **not** circular.

**Constraints:**

*   `1 <= sentence.length <= 500`
*   `sentence` consist of only lowercase and uppercase English letters and spaces.
*   The words in `sentence` are separated by a single space.
*   There are no leading or trailing spaces.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_circular

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Scan the sentence string — at every space, check that the character before it equals the character after it, then check first and last characters match for wrap-around. O(n) time, O(1) space. Tests should cover single words, case sensitivity, and basic circular/non-circular cases.

[Committed changes to planner branch]