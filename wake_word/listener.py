from struct import unpack_from

import pvporcupine

access_key = "5VYNKOfZXNH2M0vgdkLpq+6Kukwp92DXYfYDoXd0FPUMtRUmKLpY3A=="


class Listener:
    def __init__(self):
        self._handler = pvporcupine.create(
            access_key=access_key,
            keyword_paths=['/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/Hey-Julia_en_mac_v3_0_0/Hey-Julia_en_mac_v3_0_0.ppn'])

    def wake_up(self, audio):
        pcm = unpack_from("h" * self._handler.frame_length, audio)
        keyword_index = self._handler.process(pcm)
        if keyword_index >= 0:
            return True

        return False
