from pydantic import BaseModel


class JokerConfig(BaseModel):
    file_path: str = "/Users/denizulcay/code/local/aws-sample-scripts/resources/jokes/jokes.json"
