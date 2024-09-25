from typing import Literal

from task_registry.task._base import BaseTaskRequest, BaseTaskResponse
from task_registry.task.translation.const import GET_TRANSLATION_REQUEST, GET_TRANSLATION_RESPONSE, _LANGUAGE_TO_CODE


class GetTranslationRequest(BaseTaskRequest):
    request_type: Literal[GET_TRANSLATION_REQUEST]
    from_lang: Literal['en', 'tr'] = 'en'
    to_lang: Literal['en', 'tr']
    payload: str


class GetTranslationResponse(BaseTaskResponse):
    response_type: Literal[GET_TRANSLATION_RESPONSE]
    result: str


def build_get_translation_request(text: str) -> GetTranslationRequest:
    words = text.split(' ')

    to_language = words[words.index("to") + 1]
    to_lang = _LANGUAGE_TO_CODE[to_language]

    from_language = words[words.index("from") + 1]
    from_lang = _LANGUAGE_TO_CODE[from_language]

    payload = text.split(to_language)[-1]

    return GetTranslationRequest(
        request_type=GET_TRANSLATION_REQUEST,
        payload=payload,
        from_lang=from_lang,
        to_lang=to_lang
    )
