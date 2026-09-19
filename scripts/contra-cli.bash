#!/usr/bin/bash
# scripts/contra-cli.bash - Bash wrapper for Contra MCP CLI operations
set -euo pipefail
IFS=$'\n\t'

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_CLI="${SCRIPT_DIR}/contra-cli.py"

if [[ ! -x "${PYTHON_CLI}" ]]; then
   chmod +x "${PYTHON_CLI}"
fi

exec "${PYTHON_CLI}" "$@"
