import sys

import cv2

from src.streamfleet_client.domain.ports.stream_adapter import StreamAdapter


def _open_capture(device_index: int) -> cv2.VideoCapture:
    if sys.platform == "darwin":
        return cv2.VideoCapture(device_index, cv2.CAP_AVFOUNDATION)
    return cv2.VideoCapture(device_index)


def _camera_access_failed_message() -> None:
    print(
        "Webcam failed to open. On macOS: System Settings → Privacy & Security → Camera — "
        "enable the app that runs Python (Terminal, Cursor, iTerm, etc.). "
        "Then restart that app. Optional reset: tccutil reset Camera"
    )


class WebcamFrameRead:
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
        cap = _open_capture(self._device_index)
        if not cap.isOpened():
            cap.release()
            _camera_access_failed_message()
            return False
        ok, _ = cap.read()
        if not ok:
            cap.release()
            _camera_access_failed_message()
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
        return 0
