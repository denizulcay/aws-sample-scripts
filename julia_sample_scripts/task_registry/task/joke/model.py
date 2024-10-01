from typing import Literal

from julia_sample_scripts.task_registry.task._base import BaseTaskRequest, BaseTaskResponse
from julia_sample_scripts.task_registry.task.joke.const import GET_JOKE_REQUEST, GET_JOKE_RESPONSE
from julia_sample_scripts.task_registry.task.model import ReplyResult


class GetJokeRequest(BaseTaskRequest):
    request_type: Literal[GET_JOKE_REQUEST]


class GetJokeResponse(BaseTaskResponse):
    response_type: Literal[GET_JOKE_RESPONSE]
    result: ReplyResult


def build_get_joke_request(text: str) -> GetJokeRequest:
    return GetJokeRequest(request_type=GET_JOKE_REQUEST)
