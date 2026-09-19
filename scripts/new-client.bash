#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# scripts/new-client.bash - Bootstrap a new client directory and proposal dossier in valid RST

usage() {
    cat <<'EOF'
Usage:
    scripts/new-client.bash <client-slug> [Company Name]

Example:
    scripts/new-client.bash acme-corp "Acme Corporation"
EOF
    exit 1
}

make_border() {
    local len="$1"
    local char="${2:-=}"
    local border=""
    local i
    for ((i = 0; i < len; i++)); do
        border="${border}${char}"
    done
    printf '%s' "${border}"
}

set_title_block() {
    local file="$1"
    local title="$2"
    local len="${#title}"
    local border
    border="$(make_border "${len}" "=")"

    local escaped_title="${title//&/\\&}"
    local escaped_border="${border//&/\\&}"

    sed -i "1s/.*/${escaped_border}/" "${file}"
    sed -i "2s/.*/${escaped_title}/" "${file}"
    sed -i "3s/.*/${escaped_border}/" "${file}"
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
    local sow_template="${repo_root}/proposals/sow-template.rst"
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

    local escaped_company="${company_name//&/\\&}"

    # 1. Process README.rst with dynamic title borders
    sed -e "s/{{CLIENT_NAME}}/${escaped_company}/g" \
        -e "s/{{COMPANY}}/${escaped_company}/g" \
        -e "s/{{KICKOFF_DATE}}/${current_date}/g" \
        "${template_dir}/README.rst" > "${target_dir}/README.rst"
    set_title_block "${target_dir}/README.rst" "Client Dossier: ${company_name}"

    # 2. Process notes.rst with dynamic title borders
    sed -e "s/{{CLIENT_NAME}}/${escaped_company}/g" \
        "${template_dir}/notes.rst" > "${target_dir}/notes.rst"
    set_title_block "${target_dir}/notes.rst" "Working Notes & Discovery: ${company_name}"

    # 3. Process proposal.rst with dynamic title borders
    if [[ -f "${sow_template}" ]]; then
        sed -e "s/\[Client Name\]/${escaped_company}/g" \
            -e "s/\[Client Company Name\]/${escaped_company}/g" \
            -e "s/\[YYYY-MM-DD\]/${current_date}/g" \
            "${sow_template}" > "${target_dir}/proposal.rst"
        set_title_block "${target_dir}/proposal.rst" "Scope of Work (SOW): ${company_name} - [Project Title]"
    fi

    # Log with ajourn if available
    if command -v ajourn >/dev/null 2>&1; then
        (
            cd "${repo_root}"
            ajourn log -m "DEC: Onboarded new client dossier '${client_slug}' (${company_name})" -t "DEC"
        )
    fi

    echo "Successfully initialized client workspace at: ${target_dir}"
    echo "  - ${target_dir}/README.rst"
    echo "  - ${target_dir}/proposal.rst"
    echo "  - ${target_dir}/notes.rst"
}

main "$@"
