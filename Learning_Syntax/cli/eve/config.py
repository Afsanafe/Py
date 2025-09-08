# eve/config.py
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json
import os
from typing import Any, Dict, Optional

import yaml  # from PyYAML
from pydantic import BaseModel, Field, ValidationError, field_validator

# ----- Pydantic schema (validated config) -----
class Config(BaseModel):
    # Defaults your CLI can use if flags omitted
    default_name: Optional[str] = Field(None, description="Default name for greet")
    default_shout: bool = Field(False, description="Whether greet shouts by default")
    default_a: Optional[int] = Field(None, description="Default A for add")
    default_b: Optional[int] = Field(None, description="Default B for add")

    @field_validator("default_a", "default_b")
    @classmethod
    def non_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("must be >= 0")
        return v

# ----- Loader helpers -----
SEARCH_FILENAMES = (
    ".eve.yaml", ".eve.yml", ".eve.toml", ".eve.json",
    "config.yaml", "config.yml", "config.toml", "config.json",
)

def _read_yaml(p: Path) -> Dict[str, Any]:
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}

def _read_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8")) or {}

def _read_toml(p: Path) -> Dict[str, Any]:
    try:
        import tomllib  # py311+
    except ModuleNotFoundError:
        import tomli as tomllib
    return tomllib.loads(p.read_text(encoding="utf-8"))

READERS = {
    ".yaml": _read_yaml,
    ".yml": _read_yaml,
    ".json": _read_json,
    ".toml": _read_toml,
}

def discover_config_path(explicit: Optional[str]) -> Optional[Path]:
    # 1) --config PATH
    if explicit:
        p = Path(explicit).expanduser()
        return p if p.is_file() else None

    # 2) env var
    env = os.getenv("EVE_CONFIG")
    if env:
        p = Path(env).expanduser()
        if p.is_file():
            return p

    # 3) local/project then XDG
    cwd = Path(".").resolve()
    for name in SEARCH_FILENAMES:
        p = (cwd / name)
        if p.is_file():
            return p

    xdg = os.getenv("XDG_CONFIG_HOME", str(Path.home() / ".config"))
    for name in SEARCH_FILENAMES:
        p = Path(xdg) / "eve" / name
        if p.is_file():
            return p

    return None

def load_config(explicit_path: Optional[str] = None) -> Config:
    path = discover_config_path(explicit_path)
    if not path:
        return Config()  # all defaults

    reader = READERS.get(path.suffix.lower())
    if not reader:
        raise RuntimeError(f"Unsupported config extension: {path.suffix}")

    raw = reader(path)
    try:
        return Config.model_validate(raw)
    except ValidationError as e:
        # Pretty message for CLI
        raise RuntimeError(f"Invalid config at {path}:\n{e}") from e
