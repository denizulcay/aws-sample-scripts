from pathlib import Path

from pydantic import BaseModel
import yaml


class BrowserConfig(BaseModel):
    bookmarks_table: str

    @staticmethod
    def from_config():
        with open(Path(__file__).parent / 'config.yml') as file:
            config = BrowserConfig.model_validate(yaml.safe_load(file))

        return config
