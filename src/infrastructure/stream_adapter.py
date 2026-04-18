from abc import ABC, abstractmethod

class StreamAdapter(ABC):
    @abstractmethod
    def streamon(self) -> bool:
        pass

    @abstractmethod
    def streamoff(self) -> bool:
        pass

    @abstractmethod
    def get_frame_read(self):
        pass

    @abstractmethod
    def get_battery(self):
        pass