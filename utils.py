import os
import sys
import json
import subprocess
import shutil
import platform
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_base_dir() -> Path:
    return BASE_DIR

def is_windows() -> bool:
    return platform.system().lower() == "windows"

def check_command_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def run_command(cmd_list, timeout=30):
    try:
        result = subprocess.run(
            cmd_list,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            shell=is_windows()
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def load_json_file(filepath: str, default=None):
    p = Path(filepath)
    if not p.is_absolute():
        p = BASE_DIR / p
    if not p.exists():
        return default if default is not None else {}
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}

def save_json_file(filepath: str, data) -> bool:
    p = Path(filepath)
    if not p.is_absolute():
        p = BASE_DIR / p
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception:
        return False

def sanitize_text(text: str) -> str:
    if not text:
        return ""
    return text.strip()
