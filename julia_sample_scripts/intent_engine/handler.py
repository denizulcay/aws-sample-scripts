from julia_sample_scripts.intent_engine.engine import IntentEngine
from julia_sample_scripts.julia.player import play_audio, play_wav
from julia_sample_scripts.speech.gcp_speaker import GcpSpeaker
from julia_sample_scripts.task_registry.director import TaskDirector, RequestDirector
from julia_sample_scripts.task_registry.task._base import CallableResult
from julia_sample_scripts.user.recognition import add_user
from julia_sample_scripts.util.text import clean_text

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.wav'
SORRY_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/sorry.wav'


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
                    audio = self._speaker.text_to_audio(response.result.reply)
                    return audio
                    # play_wav(audio)
                    # raise EOFError()
                # else:
                #     play_audio(SORRY_PATH)
                #     raise EOFError()

    def handle_new_user(self, responses):
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
                name = text.split(' ')[-1].capitalize()
                add_user(name=name)
                audio = self._speaker.text_to_audio(f"Hello {name}. Nice to meet you.")
                play_wav(audio)
                raise EOFError()
