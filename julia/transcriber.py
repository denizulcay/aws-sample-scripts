import asyncio
import struct

from amazon_transcribe.client import TranscribeStreamingClient


class Transcriber:
    def __init__(self, region, handler_class):
        self._client = TranscribeStreamingClient(region=region)
        self._handler_class = handler_class

    async def basic_transcribe(self, sample_rate: int, recorder):
        stream = await self._client.start_stream_transcription(
            language_code="en-US",
            media_sample_rate_hz=sample_rate,
            media_encoding="pcm",
        )

        async def write_chunks():
            recorder.start_recording()
            while True:
                chunk = recorder.read_recording()
                strs = struct.pack("h" * len(chunk), *chunk)
                await stream.input_stream.send_audio_event(audio_chunk=strs)

        try:
            handler = self._handler_class(stream.output_stream)
            await asyncio.gather(write_chunks(), handler.handle_events())
        finally:
            await stream.input_stream.end_stream()
