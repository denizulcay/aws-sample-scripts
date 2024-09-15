from pydub import AudioSegment
from os import path


def m4a_to_wav(file_path: str):
    (root_path, file_extension) = path.splitext(file_path)
    AudioSegment.from_file(file_path, "m4a").export(f"{root_path}.wav", format="wav")
