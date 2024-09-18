from pvrecorder import PvRecorder


class Recorder:
    def __init__(self):
        self._recorder = PvRecorder(device_index=-1, frame_length=512)

    def __enter__(self):
        return self

    def start_recording(self):
        self._recorder.start()

    def read_recording(self):
        return self._recorder.read()

    def stop_recording(self):
        self._recorder.stop()

    def __exit__(self, exc_type, exc_value, traceback):
        self._recorder.stop()
        self._recorder.delete()
