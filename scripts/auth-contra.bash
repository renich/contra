#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# scripts/auth-contra.bash - Authorize Contra MCP via browser OAuth PKCE

main() {
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local python_auth="${script_dir}/auth-contra.py"

    if [[ ! -f "${python_auth}" ]]; then
        echo "Error: Python auth script not found at ${python_auth}" >&2
        exit 1
    fi

    chmod +x "${python_auth}"
    python3 "${python_auth}" "$@"
}

main "$@"
