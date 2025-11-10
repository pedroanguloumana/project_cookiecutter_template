from dotenv import load_dotenv
from pathlib import Path
import os

# resolve path relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
DOTENV_PATH = SCRIPT_DIR.parent / ".env"

load_dotenv(DOTENV_PATH)

PROJECT_DIR = Path(os.getenv("PROJECT_DIR"))
DATA_DIR    = Path(os.getenv("DATA_DIR"))
FIGURE_DIR  = Path(os.getenv("FIGURE_DIR"))