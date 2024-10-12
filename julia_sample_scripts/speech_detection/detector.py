import webrtcvad

from julia_sample_scripts.cli.julia_cli import SAMPLE_RATE, FRAME_LENGTH
from julia_sample_scripts.julia.microphone import MicrophoneStream
from julia_sample_scripts.wake_word.wakewordclient import WakeWordClient

vad = webrtcvad.Vad()

# Run the VAD on 10 ms of silence. The result should be False.
sample_rate = 16000
frame_duration = 30  # ms
SPEECH_FL = int(sample_rate * frame_duration / 1000)  # 480

speech_ctr = 0
wake_listener = WakeWordClient()


def extent_bytes(first, second):
    arr = bytearray()
    arr.extend(first)
    arr.extend(second)

    return bytes(arr)


awake = False
speaking = False
listening = False

with MicrophoneStream(SAMPLE_RATE, FRAME_LENGTH) as stream:
    while True:
        audio = stream.read(SPEECH_FL)
        is_speech = vad.is_speech(audio, SAMPLE_RATE)
        if is_speech:
            listening = True
            speech_ctr = 0
        else:
            speech_ctr += 1

        if speech_ctr >= 30:
            listening = False

        if listening:
            wake_audio = extent_bytes(audio, stream.read(FRAME_LENGTH - SPEECH_FL))
            awake = wake_listener.wake_up(wake_audio)
            if awake:
                print('Awake!')

print("Goodbye!")
