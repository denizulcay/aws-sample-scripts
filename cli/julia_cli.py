from client.gcp.speech_to_text.client import SpeechToTextClient
from intent_engine.handler import IntentEventHandler
from julia.microphone import MicrophoneStream
from julia.player import play_audio

from wake_word.listener import Listener

SAMPLE_RATE = 16000
HELLO_PATH = "/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/hello.wav"
FRAME_LENGTH = 512


def main():
    wake_listener = Listener()
    client = SpeechToTextClient()
    handler = IntentEventHandler()
    while True:
        awake = False
        with MicrophoneStream(SAMPLE_RATE, FRAME_LENGTH, has_callback=False) as stream:
            while not awake:
                awake = wake_listener.wake_up(stream.read())
        with MicrophoneStream(SAMPLE_RATE, FRAME_LENGTH) as stream:
            while awake:
                play_audio(HELLO_PATH)
                try:
                    responses = client.transcribe(stream.generator())
                    handler.handle(responses)
                except EOFError as e:
                    awake = False


if __name__ == "__main__":
    main()
