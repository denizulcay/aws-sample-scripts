from julia_sample_scripts.client.gcp.speech_to_text.client import SpeechToTextClient
from julia_sample_scripts.client.gcp.text_to_speech.client import TextToSpeechClient
from julia_sample_scripts.intent_engine.engine import IntentEngine
from julia_sample_scripts.task_registry.director import RequestDirector, TaskDirector
from julia_sample_scripts.util.text import clean_text
from julia_sample_scripts.wake_word.wakewordclient import WakeWordClient


HELLO_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/hello.wav'


class JuliaHandler:
    def __init__(self):
        self._wake_client = WakeWordClient()
        self._stt_client = SpeechToTextClient()
        self._tts_client = TextToSpeechClient()
        self._intent_engine = IntentEngine()

    def handle(self, request):
        pass

    def handle_transcript(self, audio: bytes) -> bytes:
        # Transcribe audio
        transcript = self._stt_client.transcribe_file(audio)
        if transcript:
            # Pre-process text
            text = clean_text(text=transcript)
            # Resolve intent
            intent = self._intent_engine.resolve(text=text)
            # Run task
            task_request = RequestDirector.handle(intent=intent, text=text)
            task_response = TaskDirector.handle(task_request)
            # Generate speech
            result = self._tts_client.synthesize_speech(task_response.result.reply)

            return result

    def handle_wake(self, audio: bytes, frame_length: int = 512) -> bytes:
        chunk_size = frame_length * 2
        num_frames = len(audio) // chunk_size
        for i in range(num_frames):
            awake = self._wake_client.wake_up(audio[i * chunk_size:i * chunk_size + chunk_size])
            if awake:
                with open(HELLO_PATH, 'rb') as f:
                    return f.read()
