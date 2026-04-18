import cv2

from src.infrastructure.stream_adapter import StreamAdapter


class WebcamFrameRead:
    """Mimics djitellopy-style frame access for the websocket loop."""

    def __init__(self, cap: cv2.VideoCapture):
        self._cap = cap

    @property
    def frame(self):
        ok, frame = self._cap.read()
        return frame if ok else None


class WebcamAdapter(StreamAdapter):
    def __init__(self, device_index: int = 0):
        self._device_index = device_index
        self._cap = None

    def streamon(self) -> bool:
        cap = cv2.VideoCapture(self._device_index)
        if not cap.isOpened():
            cap.release()
            return False
        self._cap = cap
        return True

    def streamoff(self) -> bool:
        if self._cap is not None:
            self._cap.release()
            self._cap = None
        return True

    def get_frame_read(self):
        if self._cap is None or not self._cap.isOpened():
            return None
        return WebcamFrameRead(self._cap)

    def get_battery(self):
        return 100
