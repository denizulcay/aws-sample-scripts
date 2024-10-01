from abc import ABC, abstractmethod
from typing import Union

from pydantic import BaseModel

from julia_sample_scripts.task_registry.task.model import ReplyResult, CallableResult


class BaseTaskRequest(BaseModel):
    request_type: str


class BaseTaskResponse(BaseModel):
    response_type: str
    result: Union[ReplyResult, CallableResult]


class BaseTaskHandler(ABC):
    def __init__(self, region: str = 'us-east-2'):
        self._region = region

    @abstractmethod
    def handle(self, request: BaseTaskRequest) -> BaseTaskResponse: pass
