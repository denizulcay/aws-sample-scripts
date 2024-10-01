from julia_sample_scripts.client.gcp.text_to_speech.client import TextToSpeechClient
from julia_sample_scripts.speech._base import Speaker

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.wav'


class GcpSpeaker(Speaker):
    def __init__(self):
        self._client = TextToSpeechClient()

    def text_to_audio(self, text: str):
        return self._client.synthesize_speech(text)
