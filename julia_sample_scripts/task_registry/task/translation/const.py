from typing import Dict

GET_TRANSLATION_REQUEST: str = "GET_TRANSLATION_REQUEST"
GET_TRANSLATION_RESPONSE: str = "GET_TRANSLATION_RESPONSE"

TRANSLATION: str = "TranslatedText"
TRANSLATE: str = "translate"

_LANGUAGE_TO_CODE: Dict[str, str] = {
    "english": "en",
    "turkish": "tr",
    "french": "fr",
    "spanish": "es"
}
