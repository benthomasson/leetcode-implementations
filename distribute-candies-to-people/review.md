# Review: Distribute Candies to People

## Solution
- **Approach**: Simulation loop distributing candies in increasing amounts (1, 2, 3, ...) with modulo wrapping, giving min(counter, remaining) each turn.
- **Time Complexity**: O(√candies)
- **Space Complexity**: O(num_people)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes both examples, edge cases (single person, single candy, exact exhaustion, partial last gift), invariant checks (sum preservation), and stress test (10^9 candies)
- **Edge Cases**: Yes - single person, single candy, exact round completion, two full rounds, partial last gift

## Plan
- **Quality**: Good - concise as required for MINIMAL effort level, clearly identifies O(√candies) simulation approach

## Overall
Correct implementation with comprehensive tests. The solution efficiently handles the constraint of up to 10^9 candies using the simulation approach. No issues found.
