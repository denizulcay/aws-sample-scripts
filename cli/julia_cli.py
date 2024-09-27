from client.gcp.speech_to_text.client import SpeechToTextClient
from intent_engine.handler import IntentEventHandler
from julia.microphone import MicrophoneStream
from julia.player import play_audio

from wake_word.listener import Listener

SAMPLE_RATE = 16000
CHUNK_SIZE = 1024 * 8
AUDIO_PATH = "/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/hello.wav"
FRAME_LENGTH = 512
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


def main():
    wake_listener = Listener()
    client = SpeechToTextClient()
    handler = IntentEventHandler()
    wake_up = False
    with MicrophoneStream(RATE, FRAME_LENGTH, wake_listener._handler) as stream:
        while not wake_up:
            wake_up = wake_listener.wake_up(stream.read())

    with MicrophoneStream(RATE, FRAME_LENGTH) as stream:
        play_audio(AUDIO_PATH)
        try:
            responses = client.transcribee(stream.generator())
            handler.handle(responses)
        except Exception as e:
            print(e)
            raise e


if __name__ == "__main__":
    main()
