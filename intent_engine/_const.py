from task_registry.task.browser.const import LAUNCH_BOOKMARK_REQUEST
from task_registry.task.joke.const import GET_JOKE_REQUEST
from task_registry.task.translation.const import GET_TRANSLATION_REQUEST

_CLASSIFY_MAP = {
    GET_JOKE_REQUEST: lambda x: x in ["tell me a joke"],
    GET_TRANSLATION_REQUEST: lambda x: x.startswith("translate"),
    LAUNCH_BOOKMARK_REQUEST: lambda x: x.startswith("browse"),
}
