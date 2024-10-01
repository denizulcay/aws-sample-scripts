import json
from random import choice
from typing import List

from julia_sample_scripts.task_registry.task._base import BaseTaskHandler
from julia_sample_scripts.task_registry.task.joke.config import JokerConfig
from julia_sample_scripts.task_registry.task.joke.const import GET_JOKE_RESPONSE
from julia_sample_scripts.task_registry.task.joke.model import GetJokeRequest, GetJokeResponse
from julia_sample_scripts.task_registry.task.model import ReplyResult, REPLY_RESULT


class GetJokeHandler(BaseTaskHandler):
    def __init__(self, region='us-east-2'):
        super().__init__(region=region)
        self._config: JokerConfig = JokerConfig()

    def handle(self, request: GetJokeRequest) -> GetJokeResponse:
        config: JokerConfig = self._config
        print(config.file_path)
        with open(config.file_path, 'r') as f:
            jokes: List[str] = json.load(f)

        return GetJokeResponse(
            response_type=GET_JOKE_RESPONSE,
            result=ReplyResult(
                result_type=REPLY_RESULT,
                reply=choice(jokes)
            )
        )
