# Plan (Iteration 1)

Task: Solve the LeetCode problem "alternating-digit-sum":

You are given a positive integer `n`. Each digit of `n` has a sign according to the following rules:

*   The **most significant digit** is assigned a **positive** sign.
*   Each other digit has an opposite sign to its adjacent digits.

Return _the sum of all digits with their corresponding sign_.

**Example 1:**

**Input:** n = 521
**Output:** 4
**Explanation:** (+5) + (-2) + (+1) = 4.

**Example 2:**

**Input:** n = 111
**Output:** 1
**Explanation:** (+1) + (-1) + (+1) = 1.

**Example 3:**

**Input:** n = 886996
**Output:** 0
**Explanation:** (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.

**Constraints:**

*   `1 <= n <= 109`

.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; } .spoiler {overflow:hidden;} .spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;} .spoilerbutton\[value="Show Message"\] + .spoiler > div {margin-top:-500%;} .spoilerbutton\[value="Hide Message"\] + .spoiler {padding:5px;}

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sum_of_digits

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The problem is straightforward — string conversion with alternating signs, O(d) complexity. Ready for implementation.

[Committed changes to planner branch]