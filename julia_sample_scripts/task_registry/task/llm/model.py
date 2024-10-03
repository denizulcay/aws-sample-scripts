from typing import Literal

from julia_sample_scripts.task_registry.task._base import BaseTaskResponse, BaseLongTaskRequest
from julia_sample_scripts.task_registry.task.llm.const import GET_LLM_ANSWER_REQUEST, GET_LLM_ANSWER_RESPONSE


class GetLlmAnswerRequest(BaseLongTaskRequest):
    request_type: Literal[GET_LLM_ANSWER_REQUEST]
    text: str


class GetLlmAnswerResponse(BaseTaskResponse):
    response_type: Literal[GET_LLM_ANSWER_RESPONSE]


def build_get_llm_answer_request(text: str) -> GetLlmAnswerRequest:
    text = text.replace("answer me this ", "")
    return GetLlmAnswerRequest(request_type=GET_LLM_ANSWER_REQUEST, text=text)
