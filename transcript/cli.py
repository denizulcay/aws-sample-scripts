from transcript.player import play_audio
from transcript.transcriber import Transcriber
from transcript.speaker import SpeakEventHandler
import asyncio
from time import time

# start_time = time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(basic_transcribe())
# loop.close()
# play_audio('/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.mp3')
# end_time = time()
# time_delta = end_time - start_time
# print(f"Time taken: {time_delta}")


SAMPLE_RATE = 48000
CHUNK_SIZE = 10240 * 8
AUDIO_PATH = "/Users/denizulcay/code/local/aws-sample-scripts/resources/recording.wav"


start_time = time()
transcriber = Transcriber("us-east-2", SpeakEventHandler)
loop = asyncio.get_event_loop()
loop.run_until_complete(
    transcriber.basic_transcribe(
        sample_rate=SAMPLE_RATE,
        chunk_size=CHUNK_SIZE,
        audio_path=AUDIO_PATH
    )
)
loop.close()
play_audio('/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.mp3')
end_time = time()
time_delta = end_time - start_time
print(f"Time taken: {time_delta}")

