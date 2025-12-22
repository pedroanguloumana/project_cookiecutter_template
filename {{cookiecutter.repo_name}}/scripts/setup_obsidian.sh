#!/usr/bin/env bash
set -euo pipefail

ORIGINAL_DIR="$(pwd)"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

repo_name="{{ cookiecutter.repo_name }}"

vault_note_dir="$HOME/Vault/06-Project_Notes/$repo_name"
repo_dir="$HOME/Projects/$repo_name"

mkdir -p "$vault_note_dir"

# Create/overwrite the vault note with a header
printf '# %s\n' "{{ cookiecutter.repo_name }}" > "$vault_note_dir/Progress_Log.md"

# Symlink in the repo -> vault note
touch "$vault_note_dir/Progress_Log.md"
ln -sf "$vault_note_dir/Progress_Log.md" "$repo_dir/Progress_Log.md"

# Symlink in the vault -> repo figures directory
ln -sfn "$repo_dir/figures" "$vault_note_dir/figures"

cd "$ORIGINAL_DIR"
