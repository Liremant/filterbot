import json
from pathlib import Path

CONFIG_PATH = Path("config.json")

REGEX_PATH = Path("regex.json")


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_regex() -> dict:
    with REGEX_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


config = load_config()
regex = load_regex()
