#!/usr/bin/env bash
set -e

ORIGINAL_DIR="$(pwd)"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

repo_name="{{ cookiecutter.repo_name }}"

project_folder_name="$HOME/Vault/06-Project_Notes/$repo_name"

mkdir -p "$project_folder_name"

ln -sf "$HOME/Projects/$repo_name/Progress_Log.md" "$project_folder_name/Progress_Log.md"
ln -sfn "$HOME/Projects/$repo_name/figures"         "$project_folder_name/figures"

cd "$ORIGINAL_DIR"
