from julia_sample_scripts.client.gcp.geminiai.client import GeminiAiClient
from julia_sample_scripts.task_registry.task._base import BaseTaskHandler
from julia_sample_scripts.task_registry.task.llm.const import GET_LLM_ANSWER_RESPONSE
from julia_sample_scripts.task_registry.task.llm.model import GetLlmAnswerRequest, GetLlmAnswerResponse
from julia_sample_scripts.task_registry.task.model import ReplyResult, REPLY_RESULT


class LlmHandler(BaseTaskHandler):
    def __init__(self, region: str = 'us-east-2'):
        super().__init__(region)
        self._client = GeminiAiClient()

    def handle(self, request: GetLlmAnswerRequest) -> GetLlmAnswerResponse:
        answer = self._client.generate_content(prompt=request.text)
        answer = answer.replace("", "*").replace("", "#")
        return GetLlmAnswerResponse(
            response_type=GET_LLM_ANSWER_RESPONSE,
            result=ReplyResult(
                result_type=REPLY_RESULT,
                reply=answer
            )
        )
