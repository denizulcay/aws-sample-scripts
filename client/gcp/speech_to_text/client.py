from google.cloud.speech import SpeechClient, RecognitionAudio, RecognitionConfig, StreamingRecognizeRequest, StreamingRecognitionConfig

RATE = 16000


class SpeechToTextClient:
    def __init__(self):
        self._client = SpeechClient()
        self._config = RecognitionConfig(
            encoding=RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code="en-US",
        )
        self._streaming_config = StreamingRecognitionConfig(
            config=self._config,
            interim_results=True
        )

    def transcribe(self, audio_chunk):
        requests = [StreamingRecognizeRequest(audio_content=audio_chunk)]
        responses = self._client.streaming_recognize(self._streaming_config, requests)

        return responses

    def transcribee(self, generator):
        requests = (
            StreamingRecognizeRequest(audio_content=content)
            for content in generator
        )
        responses = self._client.streaming_recognize(self._streaming_config, requests)

        return responses

    def transcribe_file(self, audio_chunk):
        audio = RecognitionAudio(content=audio_chunk)
        response = self._client.recognize(config=self._config, audio=audio)

        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
