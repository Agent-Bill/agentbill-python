#!/usr/bin/env bash
# Lightweight cleanup script for a Python repo.
# CAUTION: inspect the commands before running in production repos.

set -euo pipefail

# Preview vs apply
DRY_RUN=${DRY_RUN:-1}

echo "Dry run mode: $DRY_RUN (set DRY_RUN=0 to actually delete files)"

# Patterns to remove
PATTERNS=(
  ".pytest_cache"
  ".mypy_cache"
  "build"
  "dist"
  "*.egg-info"
)

for p in "${PATTERNS[@]}"; do
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "[DRY] would remove: $p"
  else
    echo "Removing: $p"
    rm -rf $p || true
  fi
done

# remove __pycache__ and .pyc files
if [ "$DRY_RUN" -eq 1 ]; then
  echo "[DRY] would find and remove __pycache__ directories and .pyc files"
  find . -type d -name "__pycache__" -print
  find . -name "*.pyc" -print
else
  find . -type d -name "__pycache__" -exec rm -rf {} +
  find . -name "*.pyc" -delete
fi

# Optional: remove common virtualenv names (preview by default)
VENV_DIRS=( ".venv" "venv" "env" ".env" )
for d in "${VENV_DIRS[@]}"; do
  if [ -d "$d" ]; then
    if [ "$DRY_RUN" -eq 1 ]; then
      echo "[DRY] would remove virtualenv dir: $d"
    else
      echo "Removing virtualenv dir: $d"
      rm -rf "$d"
    fi
  fi
done

# Run formatters & linters (only if not dry-run)
if [ "$DRY_RUN" -eq 0 ]; then
  echo "Running ruff --fix"
  ruff --fix .

  echo "Running isort"
  isort --profile black .

  echo "Running black"
  black .
else
  echo "[DRY] would run ruff --fix, isort, black (set DRY_RUN=0 to run)"
fi

echo "Done. Inspect changes, run tests, then git add/commit as appropriate."