import asyncio

import aiofile
from amazon_transcribe.client import TranscribeStreamingClient


class Transcriber:
    def __init__(self, region, handler_class):
        self._client = TranscribeStreamingClient(region=region)
        self._handler_class = handler_class

    async def basic_transcribe(self, sample_rate: int, audio_path: str, chunk_size: int):
        # Start transcription to generate our async stream
        stream = await self._client.start_stream_transcription(
            language_code="en-US",
            media_sample_rate_hz=sample_rate,
            media_encoding="pcm",
        )

        async def write_chunks():
            async with aiofile.AIOFile(audio_path, "rb") as afp:
                reader = aiofile.Reader(afp, chunk_size=chunk_size)
                async for chunk in reader:
                    await stream.input_stream.send_audio_event(audio_chunk=chunk)
            await stream.input_stream.end_stream()

        # Instantiate our handler and start processing events
        handler = self._handler_class(stream.output_stream)
        await asyncio.gather(write_chunks(), handler.handle_events())
