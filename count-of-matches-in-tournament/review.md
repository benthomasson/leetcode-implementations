# Review: Count of Matches in Tournament

## Solution
- **Approach**: Mathematical insight - each match eliminates exactly one team, so n-1 matches are needed to determine a winner from n teams
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes both problem examples, edge cases (n=1, n=2), boundary case (n=200), and tests both odd/even team counts
- **Edge Cases**: Yes - covers single team (0 matches), two teams (1 match), and maximum constraint (200 teams)

## Plan
- **Quality**: Good - correctly identifies the key mathematical insight that each match eliminates one team, avoiding unnecessary simulation

## Overall
Excellent solution that transforms a potential simulation problem into a trivial O(1) operation using mathematical reasoning. Test coverage is comprehensive with proper edge case handling.
