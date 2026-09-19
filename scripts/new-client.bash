#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# scripts/new-client.bash - Bootstrap a new client directory and proposal dossier

usage() {
    cat <<'EOF'
Usage:
    scripts/new-client.bash <client-slug> [Company Name]

Example:
    scripts/new-client.bash acme-corp "Acme Corporation"
EOF
    exit 1
}

main() {
    if [[ $# -lt 1 ]]; then
        usage
    fi

    local client_slug="$1"
    local company_name="${2:-$client_slug}"
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local repo_root
    repo_root="$(cd "${script_dir}/.." && pwd)"
    local template_dir="${repo_root}/clients/_template"
    local target_dir="${repo_root}/clients/${client_slug}"
    local sow_template="${repo_root}/proposals/sow-template.md"
    local current_date
    current_date="$(date +%Y-%m-%d)"

    if [[ -d "${target_dir}" ]]; then
        echo "Error: Target directory '${target_dir}' already exists." >&2
        exit 1
    fi

    if [[ ! -d "${template_dir}" ]]; then
        echo "Error: Template directory '${template_dir}' not found." >&2
        exit 1
    fi

    echo "Creating client workspace for '${client_slug}'..."
    mkdir -p "${target_dir}"

    # Copy templates
    sed -e "s/{{CLIENT_NAME}}/${company_name}/g" \
        -e "s/{{COMPANY}}/${company_name}/g" \
        -e "s/{{KICKOFF_DATE}}/${current_date}/g" \
        "${template_dir}/README.md" > "${target_dir}/README.md"

    sed -e "s/{{CLIENT_NAME}}/${company_name}/g" \
        "${template_dir}/notes.md" > "${target_dir}/notes.md"

    if [[ -f "${sow_template}" ]]; then
        sed -e "s/\[Client Name\]/${company_name}/g" \
            -e "s/\[Client Company Name\]/${company_name}/g" \
            -e "s/\[YYYY-MM-DD\]/${current_date}/g" \
            "${sow_template}" > "${target_dir}/proposal.md"
    fi

    # Log with ajourn if available
    if command -v ajourn >/dev/null 2>&1; then
        (
            cd "${repo_root}"
            ajourn log -m "DEC: Onboarded new client dossier '${client_slug}' (${company_name})" -t "DEC"
        )
    fi

    echo "Successfully initialized client workspace at: ${target_dir}"
    echo "  - ${target_dir}/README.md"
    echo "  - ${target_dir}/proposal.md"
    echo "  - ${target_dir}/notes.md"
}

main "$@"
