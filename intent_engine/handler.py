from intent_engine.engine import IntentEngine
from julia.player import play_audio
from speech.gcp_speaker import GcpSpeaker
from task_registry.director import TaskDirector, RequestDirector
from task_registry.task._base import CallableResult
from util.text import clean_text

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.wav'
SORRY_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/sorry.wav'

# class IntentEventHandler(TranscriptResultStreamHandler):
#     def __init__(self, transcript_result_stream: TranscriptResultStream):
#         super().__init__(transcript_result_stream)
#         self._speaker = GcpSpeaker()
#
#     async def handle_transcript_event(self, transcript_event: TranscriptEvent):
#         results = transcript_event.transcript.results
#         for result in results:
#             for alt in result.alternatives:
#                 if not result.is_partial:
#                     print(alt.transcript)
#                     text = clean_text(text=alt.transcript)
#                     intent = IntentEngine.resolve(text=text)
#                     request = RequestDirector.handle(intent=intent, text=text)
#                     response = TaskDirector.handle(request)
#
#                     if isinstance(response.result, CallableResult):
#                         response.result.callback_function(**response.result.kwargs)
#                     self._speaker.text_to_audio(response.result.reply)
#                     play_audio(DST_PATH)
#                     raise EOFError()
#

class IntentEventHandler:
    def __init__(self):
        self._speaker = GcpSpeaker()

    def handle(self, responses):
        for response in responses:
            if not response.results:
                continue

            result = response.results[0]
            if not result.alternatives:
                continue

            transcript = result.alternatives[0].transcript

            if result.is_final:
                print(transcript)
                text = clean_text(text=transcript)
                intent = IntentEngine.resolve(text=text)
                if intent:
                    request = RequestDirector.handle(intent=intent, text=text)
                    response = TaskDirector.handle(request)
                    if isinstance(response.result, CallableResult):
                        response.result.callback_function(**response.result.kwargs)
                    self._speaker.text_to_audio(response.result.reply)
                    play_audio(DST_PATH)
                    raise EOFError()
                else:
                    play_audio(SORRY_PATH)
