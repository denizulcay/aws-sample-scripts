from abc import ABC

import boto3

from task_registry.task._base import BaseTaskHandler
from task_registry.task.translation.const import TRANSLATION, TRANSLATE, GET_TRANSLATION_RESPONSE
from task_registry.task.translation.model import GetTranslationRequest, GetTranslationResponse


class BaseTranslationHandler(BaseTaskHandler, ABC):
    def __init__(self, config):
        super().__init__(config)
        self._client = boto3.Session(region_name='us-east-2').client(TRANSLATE)


class GetTranslationHandler(BaseTranslationHandler):
    def handle(self, request: GetTranslationRequest) -> GetTranslationResponse:
        return GetTranslationResponse(
            response_type=GET_TRANSLATION_RESPONSE,
            result=self._client.translate_text(
                Text=request.payload,
                SourceLanguageCode=request.from_lang,
                TargetLanguageCode=request.to_lang,
            )[TRANSLATION]
        )
