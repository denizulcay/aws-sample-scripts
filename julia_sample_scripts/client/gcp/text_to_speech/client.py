from google.cloud import texttospeech


class TextToSpeechClient:
    def __init__(self):
        self._client = texttospeech.TextToSpeechClient()
        self._voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Journey-O"
        )
        self._audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

    def synthesize_speech(self, text) -> bytes:
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self._client.synthesize_speech(
            input=synthesis_input, voice=self._voice, audio_config=self._audio_config
        )
        return response.audio_content
