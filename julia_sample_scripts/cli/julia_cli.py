from julia_sample_scripts.client.gcp.speech_to_text.client import SpeechToTextClient
from julia_sample_scripts.client.gcp.text_to_speech.client import TextToSpeechClient
from julia_sample_scripts.intent_engine.handler import IntentEventHandler
from julia_sample_scripts.julia.microphone import MicrophoneStream
from julia_sample_scripts.julia.player import play_wav
from julia_sample_scripts.user.recognition import recognize_user

from julia_sample_scripts.wake_word.listener import Listener

SAMPLE_RATE = 16000
FRAME_LENGTH = 512


def main():
    wake_listener = Listener()
    client = SpeechToTextClient()
    speech_client = TextToSpeechClient()
    handler = IntentEventHandler()
    user = recognize_user()
    if not user:
        with MicrophoneStream(SAMPLE_RATE, FRAME_LENGTH) as stream:
            speech = speech_client.synthesize_speech(
                f"Hello. I don't think we've met before. My name is Julia. What is your name?"
            )
            play_wav(speech)
            try:
                responses = client.transcribe(stream.generator())
                handler.handle_new_user(responses)
            except EOFError as e:
                pass
    else:
        speech = speech_client.synthesize_speech(f"Hello {user}. How may I help you today?")
        play_wav(speech)
    awake = False
    while True:
        with MicrophoneStream(SAMPLE_RATE, FRAME_LENGTH, has_callback=False) as stream:
            while not awake:
                awake = wake_listener.wake_up(stream.read())
        with MicrophoneStream(SAMPLE_RATE, FRAME_LENGTH) as stream:
            try:
                speech = speech_client.synthesize_speech(f"Hello {user}.")
                play_wav(speech)
                responses = client.transcribe(stream.generator())
                handler.handle(responses)
            except EOFError as e:
                awake = False


if __name__ == "__main__":
    main()
