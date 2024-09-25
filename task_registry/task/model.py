from typing import Literal, Callable

from pydantic import BaseModel

REPLY_RESULT = "reply"
CALLABLE_RESULT = "callable"


class ReplyResult(BaseModel):
    result_type: Literal[REPLY_RESULT]
    reply: str


class CallableResult(BaseModel):
    result_type: Literal[CALLABLE_RESULT]
    callback_function: Callable
    kwargs: dict
    reply: str = None
