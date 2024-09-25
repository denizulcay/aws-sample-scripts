from abc import ABC

from client.aws.dynamodb.client import DynamoDbClient
from task_registry.task._base import BaseTaskHandler
from task_registry.task.browser.config import BrowserConfig
from task_registry.task.browser.const import LAUNCH_BOOKMARK_RESPONSE, LAUNCH_URL_RESPONSE
from task_registry.task.browser.function import launch_url
from task_registry.task.browser.model import LaunchBookmarkRequest, LaunchBookmarkResponse, LaunchUrlRequest, \
    LaunchUrlResponse
from task_registry.task.model import CallableResult, CALLABLE_RESULT


class BaseBrowserHandler(BaseTaskHandler, ABC):
    def __init__(self, region: str = 'us-east-2'):
        super().__init__(region)
        self._config: BrowserConfig = BrowserConfig.from_config()
        self._db_client = DynamoDbClient(self._region)


class LaunchUrlHandler(BaseBrowserHandler):
    def handle(self, request: LaunchUrlRequest) -> LaunchUrlResponse:
        return LaunchUrlResponse(
            response_type=LAUNCH_URL_RESPONSE,
            result=CallableResult(
                result_type=CALLABLE_RESULT,
                callback_function=launch_url,
                kwargs={"url": request.url}
            )
        )


class LaunchBookmarkHandler(BaseBrowserHandler):
    def handle(self, request: LaunchBookmarkRequest) -> LaunchBookmarkResponse:
        row = self._db_client.get_row(
            table_name=self._config.bookmarks_table,
            key_col="name",
            key=request.bookmark_key
        )

        return LaunchBookmarkResponse(
            response_type=LAUNCH_BOOKMARK_RESPONSE,
            result=CallableResult(
                result_type=CALLABLE_RESULT,
                callback_function=launch_url,
                kwargs={"url": row["url"]},
                reply=f"Launching {row['display_name']}..."
            )
        )
