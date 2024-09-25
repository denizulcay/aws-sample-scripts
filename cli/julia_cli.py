from client.gcp.speech_to_text.client import SpeechToTextClient
from intent_engine.handler import IntentEventHandler
from julia.player import play_audio
from julia.recorder import Recorder
from julia.transcriber import Transcriber
import asyncio
from time import time

from wake_word.listener import Listener

SAMPLE_RATE = 16000
CHUNK_SIZE = 1024 * 8
AUDIO_PATH = "/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/hello.wav"
FRAME_LENGTH = 512


async def main():
    with Recorder() as recorder:
        recorder.start_recording()
        wake_listener = Listener()
        transcriber = Transcriber("us-east-2", IntentEventHandler)
        while True:
            recording = recorder.read_recording()
            wake_up = wake_listener.wake_up(recording)

            if wake_up:
                recorder.stop_recording()
                play_audio(AUDIO_PATH)
                await transcriber.basic_transcribe(SAMPLE_RATE, recorder)



# start_time = time()
# transcriber = Transcriber("us-east-2", IntentEventHandler)
loop = asyncio.get_event_loop()
loop.run_until_complete(
    main()
)
loop.close()
# end_time = time()
# time_delta = end_time - start_time
# print(f"Time taken: {time_delta}")


