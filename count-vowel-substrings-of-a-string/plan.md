# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-vowel-substrings-of-a-string":

A **substring** is a contiguous (non-empty) sequence of characters within a string.

A **vowel substring** is a substring that **only** consists of vowels (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) and has **all five** vowels present in it.

Given a string `word`, return _the number of **vowel substrings** in_ `word`.

**Example 1:**

**Input:** word =  "aeiouu "
**Output:** 2
**Explanation:** The vowel substrings of word are as follows (underlined):
-  "**aeiou**u "
-  "**aeiouu** "

**Example 2:**

**Input:** word =  "unicornarihan "
**Output:** 0
**Explanation:** Not all 5 vowels are present, so there are no vowel substrings.

**Example 3:**

**Input:** word =  "cuaieuouac "
**Output:** 7
**Explanation:** The vowel substrings of word are as follows (underlined):
-  "c**uaieuo**uac "
-  "c**uaieuou**ac "
-  "c**uaieuoua**c "
-  "cu**aieuo**uac "
-  "cu**aieuou**ac "
-  "cu**aieuoua**c "
-  "cua**ieuoua**c "

**Constraints:**

*   `1 <= word.length <= 100`
*   `word` consists of lowercase English letters only.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_vowel_substrings

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: O(n²) brute-force with nested loops, breaking on consonants and counting when all 5 vowels are present in the current window.

[Committed changes to planner branch]