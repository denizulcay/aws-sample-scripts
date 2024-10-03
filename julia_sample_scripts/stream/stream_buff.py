import queue
from typing import Self, Iterator


class StreamBuffer:
    def __init__(self: Self, stream_conn, chunk: int):
        self._stream = stream_conn
        self._chunk = chunk
        self.closed = True

    def __enter__(self: Self) -> Self:
        self.closed = False

        return self

    def __exit__(
        self: Self,
        type: object,
        value: object,
        traceback: object,
    ):
        self._stream.close()
        self.closed = True

    def generator(self: Self) -> Iterator[bytes]:
        while not self.closed:
            chunk = self._stream.recv(self._chunk)
            if chunk is None:
                return
            data = [chunk]
            try:
                chunk = self._stream.recv(self._chunk)
                if chunk is None:
                    return
                data.append(chunk)
            except queue.Empty:
                break

            yield b"".join(data)
