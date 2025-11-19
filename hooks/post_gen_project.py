#!/usr/bin/env python3

help = """
Your project has been created!
__________________________________________________________________________
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣞⠛⠲⠇⠉⠻⠛⢧⡻⢿
⢟⡯⠽⠒⠒⠒⠺⣟⣿⢿⠯⢉⠥⣒⣭⣥⣬⣥⡈⠈⠋⣷
⡡⠐⠊⡉⠁⠈⣀⣈⠃⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⠀⢰⡣
⠀⠀⣴⣶⣿⣿⣿⣿⣿⣿⣦⣝⢿⣿⡿⢿⣟⠋⠁⢀⣈⡿
⠀⣠⣿⡿⡫⠑⡤⡍⠻⣿⣿⣿⣯⢻⠿⠛⠁⣀⣀⡻⣵⣾
⣿⣿⣿⣧⣃⣀⣀⠀⢀⣿⣿⣿⣿⣆⠀⠐⣤⠾⢿⣵⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⠋⠁⢐⢿⠬⡾⣻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢈⣀⡀⣿⢚⠳⠯⠒⠯⡿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢳⣮⣵⣦⣾⣿⣿⣿⡆⢹
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⣴⣶⣶⣮⣉⣶⣿⣿⡿⣡⢟
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣼⣿⣿⢰⢯⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⣉⣥⣈⡛⠿⠇⣜⣼⣿
__________________________________________________________________________

IF YOU HAVE NOT DONE SO ALREADY, CREATE A CONDA ENVIRONMENT FOR YOUR NEW PROJECT WITH:

cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}}
conda activate {{cookiecutter.repo_name}}

INSTALL YOUR NEW PROJECT IN YOUR LOCAL CONDA ENVIRONMENT WITH:

pip install -e .

HAVE FUN AND GOOD LUCK

“TRUE UNDERSTANDING COMES ONLY THROUGH THE PROCESS OF THINKING ON YOUR OWN.”
— 조훈현

"""

import os
import sys
from pathlib import Path

def main():
    project_root = Path.cwd()  # This should be {{cookiecutter.repo_name}}/
    writing_path = project_root / "writing"

    # Target directory: ~/LaTeX/<repo_name>
    target_dir = Path.home() / "LaTeX" / "{{cookiecutter.repo_name}}_paper"

    # Make sure target exists
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Failed to create target directory {target_dir}: {e}", file=sys.stderr)
        return

    # Remove existing "writing" if Cookiecutter created it as a real dir
    if writing_path.is_symlink():
        writing_path.unlink()
    elif writing_path.exists():
        # Only safe if it's empty; adjust if you expect contents
        try:
            writing_path.rmdir()
        except OSError:
            print(
                f'"writing" is not empty, not replacing with symlink. '
                f'Path: {writing_path}',
                file=sys.stderr,
            )
            return

    # Create the symlink
    try:
        writing_path.symlink_to(target_dir)
        print(f"Created symbolic link: {writing_path} -> {target_dir}")
    except OSError as e:
        print(f"Failed to create symlink {writing_path} -> {target_dir}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
    # print(help)
