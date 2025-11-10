#!/usr/bin/env bash

# Usage: source scripts/setup_env.sh

# Resolve project directory for env variables
SOURCE_DIR="$0"
SCRIPT_DIR="$(cd "$(dirname "$SOURCE_DIR")" >/dev/null 2>&1 && pwd -P)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." >/dev/null 2>&1 && pwd -P)"

export PROJECT_DIR
export DATA_DIR="$PROJECT_DIR/data"
export FIGURE_DIR="$PROJECT_DIR/figures"

# Conda environment name based on project name
CONDA_ENV="{{ cookiecutter.project_name.lower().replace(' ', '_') }}"

# Load and activate conda if available
if command -v conda >/dev/null 2>&1; then
  # Load conda in current shell
  . "$(conda info --base)/etc/profile.d/conda.sh"

  if conda env list | grep -qE "^${CONDA_ENV}[[:space:]]"; then
    conda activate "$CONDA_ENV"
    echo "Activated conda environment: $CONDA_ENV"
  else
    echo "Conda environment '$CONDA_ENV' does not exist."
    echo "Create it with: conda create -n {{ cookiecutter.project_name.lower().replace(' ', '_') }}"
  fi
else
  echo "conda not found. Skipping environment activation."
fi

# Create .env if it doesn't exist
if [ ! -f "$PROJECT_DIR/.env" ]; then
  cat > "$PROJECT_DIR/.env" <<EOF
# Auto-generated on first run. Add secrets manually.
PROJECT_DIR=$PROJECT_DIR
DATA_DIR=$DATA_DIR
FIGURE_DIR=$FIGURE_DIR
EOF

  chmod 600 "$PROJECT_DIR/.env"
  echo "Created $PROJECT_DIR/.env (secrets left blank)."
else
  echo ".env already exists — not overwriting."
fi
