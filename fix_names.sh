#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
FIXED=0
SKIP=0
ERR=0

# Only process directories whose review flagged "Has Issues"
for review in "$ROOT"/*/review.md; do
  dir=$(dirname "$review")
  name=$(basename "$dir")

  # Skip if review doesn't mention naming issues
  if ! grep -q "Has Issues" "$review" 2>/dev/null; then
    continue
  fi
  if ! grep -qi "function name\|method name\|misnamed\|wrong.*name\|named.*wrong\|name.*incorrect\|incorrect.*name\|name.*mismatch\|wrong problem" "$review" 2>/dev/null; then
    SKIP=$((SKIP + 1))
    printf "s"
    continue
  fi

  # Build input with all files
  input=""
  for f in solution.py test_solution.py; do
    if [ -f "$dir/$f" ]; then
      input="$input
=== $f ===
$(cat "$dir/$f")

"
    fi
  done

  prompt="The problem slug is: $name

The function/method name in this solution is wrong — it was copied from a different LeetCode problem. Rename it to match this problem's slug. Use snake_case for standalone functions or camelCase for methods inside class Solution, matching whichever style the code already uses.

Output ONLY the corrected file contents, separated by the exact markers shown below. Do not add commentary, explanations, or markdown fences.

=== solution.py ===
(corrected solution.py contents here)

=== test_solution.py ===
(corrected test_solution.py contents here)

Rules:
- Only rename the function/method and update all references (imports, calls, etc.)
- Do NOT change any logic, comments, docstrings, or formatting
- If docstrings mention the wrong function name, fix those too
- Keep everything else exactly as-is"

  if output=$(echo "$input" | claude -p --model sonnet "$prompt" 2>/dev/null); then
    # Extract solution.py content
    sol=$(echo "$output" | sed -n '/^=== solution\.py ===/,/^=== test_solution\.py ===/{ /^=== /d; p; }')
    # Extract test_solution.py content
    test=$(echo "$output" | sed -n '/^=== test_solution\.py ===/,$ { /^=== /d; p; }')

    if [ -n "$sol" ]; then
      printf '%s\n' "$sol" > "$dir/solution.py"
    fi
    if [ -n "$test" ] && [ -f "$dir/test_solution.py" ]; then
      printf '%s\n' "$test" > "$dir/test_solution.py"
    fi

    FIXED=$((FIXED + 1))
    printf "."
  else
    ERR=$((ERR + 1))
    printf "E"
    echo "  ERROR: $name" >&2
  fi
done

echo
echo "Done: $FIXED fixed, $SKIP skipped (non-naming issue), $ERR errors"
