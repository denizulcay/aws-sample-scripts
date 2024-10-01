from playsound3 import playsound
from pydub import AudioSegment
from io import BytesIO

from pydub.playback import play


def play_audio(audio_file):
    playsound(audio_file, block=True)


def play_wav(audio: bytes):
    segment = AudioSegment.from_file(BytesIO(audio), format="wav")
    play(segment)
