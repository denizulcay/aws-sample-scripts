from abc import ABC, abstractmethod


class Speaker(ABC):
    @abstractmethod
    def text_to_audio(self, text): pass
