#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
PROMPT_FILE="$ROOT/test_prompt.txt"
DONE=0
ERR=0

for dir in "$ROOT"/*/; do
  [ -f "$dir/solution.py" ] || continue
  [ -f "$dir/test_solution.py" ] && continue
  name=$(basename "$dir")

  input="=== solution.py ===
$(cat "$dir/solution.py")"

  if [ -f "$dir/plan.md" ]; then
    input="$input

=== plan.md ===
$(cat "$dir/plan.md")"
  fi

  prompt=$(cat "$PROMPT_FILE")

  if test_content=$(echo "$input" | claude -p --model sonnet "$prompt" 2>/dev/null); then
    printf '%s\n' "$test_content" > "$dir/test_solution.py"
    DONE=$((DONE + 1))
    echo "OK: $name"
  else
    ERR=$((ERR + 1))
    echo "ERROR: $name"
  fi
done

echo
echo "Done: $DONE written, $ERR errors"
