from typing import Literal

from task_registry.task._base import BaseTaskRequest, BaseTaskResponse
from task_registry.task.browser.const import LAUNCH_BOOKMARK_REQUEST, LAUNCH_BOOKMARK_RESPONSE, LAUNCH_URL_RESPONSE, \
    LAUNCH_URL_REQUEST
from task_registry.task.model import CallableResult


class LaunchBookmarkRequest(BaseTaskRequest):
    request_type: Literal[LAUNCH_BOOKMARK_REQUEST]
    bookmark_key: str


class LaunchBookmarkResponse(BaseTaskResponse):
    response_type: Literal[LAUNCH_BOOKMARK_RESPONSE]
    result: CallableResult


class LaunchUrlRequest(BaseTaskRequest):
    request_type: Literal[LAUNCH_URL_REQUEST]
    url: str


class LaunchUrlResponse(BaseTaskResponse):
    response_type: Literal[LAUNCH_URL_RESPONSE]
    result: CallableResult


def build_launch_bookmark_request(text: str) -> LaunchBookmarkRequest:
    words = text.split(" ")
    return LaunchBookmarkRequest(request_type=LAUNCH_BOOKMARK_REQUEST, bookmark_key=words[1])
