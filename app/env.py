"""
Environment configuration loader.
Reads .env if present and populates os.environ without requiring external packages.
"""
import os
from pathlib import Path
from typing import Optional


def load_env_file(env_path: Optional[Path] = None):
    p = env_path if env_path else Path(__file__).resolve().parent.parent / ".env"
    if not p.exists():
        return
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip("'\"")
                if key and key not in os.environ:
                    os.environ[key] = val


load_env_file()
