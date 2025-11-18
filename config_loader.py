# config_loader.py
import json
import re
from pathlib import Path


class RegexConfig:
    def __init__(self, path: Path):
        self.path = path
        self._regex = {}
        self._patterns = []
        self.load()

    def load(self):
        """Загрузить/перезагрузить конфиг из файла"""
        with self.path.open("r", encoding="utf-8") as f:
            self._regex = json.load(f)
        self._patterns = [
            re.compile(p, re.IGNORECASE) for p in self._regex.get("expressions", [])
        ]

    def find_match(self, text: str):
        for pattern in self._patterns:
            match = pattern.search(text)
            if match:
                return pattern, match
        return None, None

    @property
    def patterns(self):
        """Всегда актуальный список паттернов"""
        return self._patterns

    @property
    def expressions(self):
        return self._regex.get("expressions", [])


class Config:
    def __init__(self, path: Path):
        self.path = path
        self._settings = {}

    def load(self):
        with self.path.open("r", encoding="utf-8") as f:
            self._config = json.load(f)

    @property
    def bot_exceptions(self):
        return self._settings.get("bot_exceptions", [])


regex_config = RegexConfig(Path("regex.json"))
config = Config(Path("config.json"))
