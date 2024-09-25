from typing import Callable, Tuple

from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

from intent_engine.engine import IntentEngine
from julia.player import play_audio
from speech.aws_speaker import AwsSpeaker
from speech.gcp_speaker import GcpSpeaker
from task_registry.director import TaskDirector, RequestDirector
from task_registry.task._base import CallableResult
from util.text import clean_text

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.wav'


class IntentEventHandler(TranscriptResultStreamHandler):
    def __init__(self, transcript_result_stream: TranscriptResultStream):
        super().__init__(transcript_result_stream)
        self._speaker = GcpSpeaker()

    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                if not result.is_partial:
                    try:
                        print(alt.transcript)
                        text = clean_text(text=alt.transcript)
                        intent = IntentEngine.resolve(text=text)
                        request = RequestDirector.handle(intent=intent, text=text)
                        response = TaskDirector.handle(request)

                        if isinstance(response.result, CallableResult):
                            response.result.callback_function(**response.result.kwargs)
                        self._speaker.text_to_audio(response.result.reply)
                        play_audio(DST_PATH)

                    except Exception as e:
                        print(e)
