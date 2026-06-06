# Plan (Iteration 1)

Task: Solve the LeetCode problem "prime-arrangements":

Return the number of permutations of 1 to `n` so that prime numbers are at prime indices (1-indexed.)

_(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)_

Since the answer may be large, return the answer **modulo `10^9 + 7`**.

**Example 1:**

**Input:** n = 5
**Output:** 12
**Explanation:** For example \[1,2,5,4,3\] is a valid permutation, but \[5,2,3,4,1\] is not because the prime number 5 is at index 1.

**Example 2:**

**Input:** n = 100
**Output:** 682289015

**Constraints:**

*   `1 <= n <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: numPrimeArrangements

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The algorithm is straightforward: count primes up to n, then return `factorial(primes) * factorial(non-primes) mod 10^9+7`.

[Committed changes to planner branch]