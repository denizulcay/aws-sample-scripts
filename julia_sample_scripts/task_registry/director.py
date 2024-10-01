from julia_sample_scripts.task_registry.task.browser.const import LAUNCH_BOOKMARK_REQUEST, LAUNCH_URL_REQUEST
from julia_sample_scripts.task_registry.task.browser.handler import LaunchBookmarkHandler, LaunchUrlHandler
from julia_sample_scripts.task_registry.task.browser.model import build_launch_bookmark_request
from julia_sample_scripts.task_registry.task.joke.const import GET_JOKE_REQUEST
from julia_sample_scripts.task_registry.task.joke.handler import GetJokeHandler
from julia_sample_scripts.task_registry.task.joke.model import build_get_joke_request
from julia_sample_scripts.task_registry.task.translation.const import GET_TRANSLATION_REQUEST
from julia_sample_scripts.task_registry.task.translation.handler import GetTranslationHandler
from julia_sample_scripts.task_registry.task.translation.model import build_get_translation_request

_REQUEST_TYPE_TO_HANDLER = {
    GET_JOKE_REQUEST: GetJokeHandler,
    GET_TRANSLATION_REQUEST: GetTranslationHandler,
    LAUNCH_BOOKMARK_REQUEST: LaunchBookmarkHandler,
    LAUNCH_URL_REQUEST: LaunchUrlHandler,
}

_REQUEST_TYPE_TO_BUILDER = {
    GET_JOKE_REQUEST: build_get_joke_request,
    GET_TRANSLATION_REQUEST: build_get_translation_request,
    LAUNCH_BOOKMARK_REQUEST: build_launch_bookmark_request
}


class TaskDirector:
    @staticmethod
    def handle(request):
        return _REQUEST_TYPE_TO_HANDLER[request.request_type]().handle(request=request)


class RequestDirector:
    @staticmethod
    def handle(intent, text):
        return _REQUEST_TYPE_TO_BUILDER[intent](text=text)
