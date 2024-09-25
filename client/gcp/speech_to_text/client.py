from struct import pack

from google.cloud.speech import SpeechClient, RecognitionAudio, RecognitionConfig


class SpeechToTextClient:
    def __init__(self):
        self._client = SpeechClient()
        self._config = RecognitionConfig(
            sample_rate_hertz=16000,
            language_code="en-US"
        )

    def transcribe(self, audio_chunk):
        packed = pack("h" * len(audio_chunk), *audio_chunk)
        audio = RecognitionAudio(packed)
        response = self._client.recognize(config=self._config, audio=audio)

        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")


