#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# scripts/build-diagrams.bash - Compile all D2 source diagrams to SVG and PNG

main() {
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local repo_root
    repo_root="$(cd "${script_dir}/.." && pwd)"
    local diagrams_dir="${repo_root}/assets/diagrams"

    if ! command -v d2 >/dev/null 2>&1; then
        echo "Error: 'd2' command not found in PATH." >&2
        exit 1
    fi

    if [[ ! -d "${diagrams_dir}" ]]; then
        echo "Error: Directory '${diagrams_dir}' not found." >&2
        exit 1
    fi

    echo "Compiling D2 diagrams in ${diagrams_dir}..."

    local d2_file
    for d2_file in "${diagrams_dir}"/*.d2; do
        if [[ ! -f "${d2_file}" ]]; then
            continue
        fi

        local base_name
        base_name="$(basename "${d2_file}" .d2)"
        local svg_out="${diagrams_dir}/${base_name}.svg"
        local png_out="${diagrams_dir}/${base_name}.png"

        echo "  [D2] ${base_name}.d2 -> SVG & PNG..."
        d2 --theme 200 --pad 20 "${d2_file}" "${svg_out}"
        d2 --theme 200 --pad 20 "${d2_file}" "${png_out}"
    done

    echo "Compilation complete. All diagram assets up to date."
}

main "$@"
