#!/usr/bin/env bash
set -euo pipefail

# Reset local JSON messages and SQLite database used by demos.
DATA_DIR="$(dirname "$0")/../data"
mkdir -p "$DATA_DIR"

# Remove messages.json and demo.db if present
rm -f "$DATA_DIR/messages.json" "$DATA_DIR/demo.db"

echo "Data reset. Removed messages.json and demo.db from $DATA_DIR"
