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

#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

def main():
    project_root = Path.cwd()  # This should be {{cookiecutter.repo_name}}/
    writing_path = project_root / "writing"

    # Target directory: ~/LaTeX/<repo_name>_paper
    target_dir = Path.home() / "LaTeX" / "{{cookiecutter.repo_name}}_paper"

    # Ensure target exists
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Failed to create target directory {target_dir}: {e}", file=sys.stderr)
        return

    # ---- Move contents of writing/ into target_dir ----
    if writing_path.exists() and writing_path.is_dir():
        for item in writing_path.iterdir():
            dest = target_dir / item.name
            try:
                shutil.move(str(item), str(dest))
                print(f"Moved {item} -> {dest}")
            except Exception as e:
                print(f"Failed to move {item} -> {dest}: {e}", file=sys.stderr)
                return
    else:
        print(f"No writing directory found at {writing_path}", file=sys.stderr)

    # Remove original writing directory (should now be empty)
    try:
        writing_path.rmdir()
    except OSError as e:
        print(f"Failed to remove original writing directory {writing_path}: {e}", file=sys.stderr)
        return

    # ---- Create the symlink ----
    try:
        writing_path.symlink_to(target_dir)
        print(f"Created symbolic link: {writing_path} -> {target_dir}")
    except OSError as e:
        print(f"Failed to create symlink {writing_path} -> {target_dir}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
