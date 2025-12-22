#!/usr/bin/env bash
set -e

# Save where the user was
ORIGINAL_DIR="$(pwd)"

# Resolve the directory this script lives in (even if called via symlink)
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Move to script directory
cd "$SCRIPT_DIR"
# --- script logic here ---
cd ~/Vaults/06-Project_Notes/
project_folder_name={{cookiecutter.project_name.replace(' ', '_')}}
mkdir $project_folder_name

ln -s ~/Projects/{{cookiecutter.project_name.replace(' ', '_')}}/Progress_Log.md ~/Vaults/06-Project_Notes/$project_folder_name/Progress_Log.md
ln -s ~/Projects/{{cookiecutter.project_name.replace(' ', '_')}}/figures/ ~/Vaults/06-Project_Notes/$project_folder_name/figures

# Return to where the user was
cd "$ORIGINAL_DIR"

