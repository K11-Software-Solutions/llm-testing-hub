#!/bin/bash

echo "[INFO] Cleaning up all results.html and .env files in $(pwd) and subfolders..."

# Delete results.html files
find . -type f -name "results.html" ! -path "*/node_modules/*" -print -exec rm -f {} \;

# Delete .env files
find . -type f -name ".env" ! -path "*/node_modules/*" -print -exec rm -f {} \;

# ==== Cleanup promptfoo-errors.log in nested folders (skip node_modules) ====
ERRCOUNT=0
while IFS= read -r file; do
  rm -f "$file"
  ERRCOUNT=$((ERRCOUNT+1))
done < <(find . -type f -name "promptfoo-errors.log" ! -path "*/node_modules/*")

echo "[INFO] Removed $ERRCOUNT promptfoo-errors.log file(s)."

echo "[INFO] Cleanup complete."
