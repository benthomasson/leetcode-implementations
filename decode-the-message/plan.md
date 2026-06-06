# Plan (Iteration 1)

Task: Solve the LeetCode problem "decode-the-message":

You are given the strings `key` and `message`, which represent a cipher key and a secret message, respectively. The steps to decode `message` are as follows:

1.  Use the **first** appearance of all 26 lowercase English letters in `key` as the **order** of the substitution table.
2.  Align the substitution table with the regular English alphabet.
3.  Each letter in `message` is then **substituted** using the table.
4.  Spaces `' '` are transformed to themselves.

*   For example, given `key = "**hap**p**y** **bo**y "` (actual key would have **at least one** instance of each letter in the alphabet), we have the partial substitution table of (`'h' -> 'a'`, `'a' -> 'b'`, `'p' -> 'c'`, `'y' -> 'd'`, `'b' -> 'e'`, `'o' -> 'f'`).

Return _the decoded message_.

**Example 1:**

**Input:** key =  "the quick brown fox jumps over the lazy dog ", message =  "vkbs bs t suepuv "
**Output:**  "this is a secret "
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in  "**the** **quick** **brown** **f**o**x** **j**u**mps** o**v**er the **lazy** **d**o**g** ".

**Example 2:**

**Input:** key =  "eljuxhpwnyrdgtqkviszcfmabo ", message =  "zwx hnfx lqantp mnoeius ycgk vcnjrdb "
**Output:**  "the five boxing wizards jump quickly "
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in  "**eljuxhpwnyrdgtqkviszcfmabo** ".

**Constraints:**

*   `26 <= key.length <= 2000`
*   `key` consists of lowercase English letters and `' '`.
*   `key` contains every letter in the English alphabet (`'a'` to `'z'`) **at least once**.
*   `1 <= message.length <= 2000`
*   `message` consists of lowercase English letters and `' '`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: valid_selections

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

**Algorithm:** Iterate through `key` to build a substitution table (first occurrence of each letter maps to 'a', 'b', 'c', ...), then substitute each letter in `message` using that table. Spaces pass through unchanged. O(n+m) time, O(1) space.

**Confidence:** HIGH — straightforward mapping problem with no algorithmic ambiguity.

[Committed changes to planner branch]