from google.cloud import texttospeech

from client.gcp.text_to_speech.client import TextToSpeechClient
from speech._base import Speaker

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.wav'


class GcpSpeaker(Speaker):
    def __init__(self):
        self._client = TextToSpeechClient()

    def text_to_audio(self, text: str):
        with open(DST_PATH, 'wb') as f:
            f.write(self._client.synthesize_speech(text))
