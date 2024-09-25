from pvrecorder import PvRecorder


class Recorder:
    def __init__(self):
        self._recorder = PvRecorder(device_index=-1, frame_length=512)
        self._is_running = False

    def __enter__(self):
        return self

    def start_recording(self):
        if not self._is_running:
            self._recorder.start()
            self._is_running = True

    def read_recording(self):
        return self._recorder.read()

    def stop_recording(self):
        if self._is_running:
            self._recorder.stop()
            self._is_running = False

    def is_running(self):
        return self._is_running

    def __exit__(self, exc_type, exc_value, traceback):
        self._recorder.stop()
        self._recorder.delete()
