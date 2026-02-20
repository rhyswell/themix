import json
import os


class ConfigLoader:
    REQUIRED_FIELDS = [
        "api_key",
        "model",
        "temperature",
        "max_output_tokens",
        "chunk_size",
        "output_directory",
        "log_level"
    ]

    @staticmethod
    def load_config(path: str = "config.json") -> dict:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file not found at {path}")

        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)

        ConfigLoader._validate(config)
        return config

    @staticmethod
    def _validate(config: dict):
        missing = [
            field for field in ConfigLoader.REQUIRED_FIELDS
            if field not in config
        ]

        if missing:
            raise ValueError(f"Missing required config fields: {missing}")