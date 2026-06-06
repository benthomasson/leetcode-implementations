# Plan (Iteration 1)

Task: Solve the LeetCode problem "number-of-segments-in-a-string":

Given a string `s`, return _the number of segments in the string_.

A **segment** is defined to be a contiguous sequence of **non-space characters**.

**Example 1:**

**Input:** s =  "Hello, my name is John "
**Output:** 5
**Explanation:** The five segments are \[ "Hello, ",  "my ",  "name ",  "is ",  "John "\]

**Example 2:**

**Input:** s =  "Hello "
**Output:** 1

**Constraints:**

*   `0 <= s.length <= 300`
*   `s` consists of lowercase and uppercase English letters, digits, or one of the following characters `"!@#$%^&*()_+-=',.: "`.
*   The only space character in `s` is `' '`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_segments

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

## PLAN

**Algorithm:** Use Python's `str.split()` with no arguments, which splits on any whitespace and discards empty strings. The segment count is simply `len(s.split())`. This is O(n) time and O(n) space. An alternative O(1) space approach counts transitions from space (or string start) to non-space character by iterating once, but `split()` is idiomatic and sufficient for n≤300.

**Implementation steps:**
1. Create `solution.py` with `count_segments(s: str) -> int` using `len(s.split())`, with a Google-style docstring.
2. Create `test_solution.py` with tests covering: normal multi-word string, single word, empty string, all spaces, leading/trailing/multiple spaces, special characters, single character, string of length 300.

**Success criteria:** All tests pass; function handles all edge cases correctly.

## SELF-REVIEW

1. **What went well:** Straightforward problem with a clean Pythonic solution.
2. **Missing info:** None needed — problem is fully specified.
3. **Next time:** Nothing — minimal problems like this don't need much planning.
4. **Confidence:** **HIGH** — trivial problem with a well-known idiomatic solution.