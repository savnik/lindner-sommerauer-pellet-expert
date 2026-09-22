#!/bin/bash
# Run an eval tier against the plugin in this repo.
#   evals/run.sh free      deterministic regression, no judge, no ablation
#   evals/run.sh judged    judged tier with ablation and a Sonnet judge
#   evals/run.sh safety    safety/privacy/consent cases, 5 runs, pass^5 gate
#   evals/run.sh case <name> [runs]   one case, one arm
set -euo pipefail
cd "$(dirname "$0")/.."
JUDGE=${EVAL_JUDGE_MODEL:-claude-sonnet-5}
COMMON=(./plugins/pellet-expert --eval-dir ../../evals/cases --no-publish --scaffold --allow-tools Write Bash)
STAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p evals/results
case "${1:-}" in
  free)   claude plugin eval "${COMMON[@]}" --tag regression --ablation none --threshold 1.0 --json "evals/results/free-$STAMP.json" ;;
  judged) claude plugin eval "${COMMON[@]}" --tag judged --ablation with-without --judge-model "$JUDGE" --threshold 0.8 --max-cost-usd "${EVAL_MAX_COST:-30}" --json "evals/results/judged-$STAMP.json" ;;
  safety) claude plugin eval "${COMMON[@]}" --tag safety --tag privacy --tag consent --runs 5 --ablation none --judge-model "$JUDGE" --threshold 1.0 --json "evals/results/safety-$STAMP.json" ;;
  case)   claude plugin eval "${COMMON[@]}" --case "$2" --runs "${3:-1}" --ablation none --judge-model "$JUDGE" --json "evals/results/case-$STAMP.json" ;;
  *) sed -n '2,6p' "$0"; exit 1 ;;
esac
