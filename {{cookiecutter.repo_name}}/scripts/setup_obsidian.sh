#!/usr/bin/env bash
set -e

# Save where the user was
ORIGINAL_DIR="$(pwd)"

# Resolve the directory this script lives in (even if called via symlink)
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Move to script directory
cd "$SCRIPT_DIR"
# --- script logic here ---
project_folder_name=~/Vaults/06-Project_Notes/{{ cookiecutter.repo_name }}"

mkdir {{ cookiecutter.repo_name }}

ln -s ~/Projects/{{cookiecutter.repo_name}}/Progress_Log.md ${{project_folder_name}}/Progress_Log.md
ln -s ~/Projects/{{cookiecutter.repo_name}}/figures/ ${{project_folder_name}}/figures

# Return to where the user was
cd "$ORIGINAL_DIR"

