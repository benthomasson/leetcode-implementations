# Review: Minimum Hours of Training to Win a Competition

## Solution
- **Approach**: Treats energy and experience independently. Energy only decreases, so requires `sum(energy) + 1` total (minus initial). Experience is simulated linearly, adding training when current experience ≤ opponent's.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes examples, boundary cases, isolated energy/experience scenarios, accumulation logic, and maximum constraints
- **Edge Cases**: Yes - tests "strictly greater" requirement, single opponent, experience accumulation, and all maximum values (n=100)

## Plan
- **Quality**: Adequate - correctly identifies the key insight about independence of energy and experience, brief as requested for minimal effort level

## Overall
Solid implementation with correct algorithm. Good test coverage including the critical "strictly greater" boundary condition and experience accumulation mechanics. Energy calculation cleverly uses the fact that only the total matters, while experience properly simulates the sequential battles.
