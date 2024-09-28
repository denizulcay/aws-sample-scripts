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
    while True:
        wake_up = False
        with MicrophoneStream(wake_listener._handler.sample_rate, wake_listener._handler.frame_length, has_callback=False) as stream:
            while not wake_up:
                wake_up = wake_listener.wake_up(stream.read())
        session = True
        with MicrophoneStream(RATE, FRAME_LENGTH) as stream:
            while session:
                play_audio(AUDIO_PATH)
                try:
                    responses = client.transcribe(stream.generator())
                    handler.handle(responses)
                except EOFError as e:
                    print(e)
                    session = False


if __name__ == "__main__":
    main()
