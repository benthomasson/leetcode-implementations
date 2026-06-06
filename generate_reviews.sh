#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
PROMPT_FILE="$ROOT/review_prompt.txt"
TOTAL=0
DONE=0
SKIP=0
ERR=0

for dir in "$ROOT"/*/; do
  [ -f "$dir/solution.py" ] || continue
  name=$(basename "$dir")
  TOTAL=$((TOTAL + 1))

  if [ -f "$dir/review.md" ]; then
    SKIP=$((SKIP + 1))
    printf "S"
    continue
  fi

  input=""
  for f in plan.md solution.py test_solution.py; do
    if [ -f "$dir/$f" ]; then
      input="$input
=== $f ===
$(cat "$dir/$f")

"
    fi
  done

  prompt=$(cat "$PROMPT_FILE")

  if review=$(echo "$input" | claude -p --model sonnet "$prompt" 2>/dev/null); then
    printf '%s\n' "$review" > "$dir/review.md"
    DONE=$((DONE + 1))
    printf "."
  else
    ERR=$((ERR + 1))
    printf "E"
    echo "  ERROR: $name" >&2
  fi

  count=$((DONE + ERR + SKIP))
  [ $((count % 80)) -eq 0 ] && [ $count -gt 0 ] && echo
done

echo
echo "Done: $DONE written, $SKIP skipped, $ERR errors (of $TOTAL total)"
