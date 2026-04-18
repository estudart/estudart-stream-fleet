import base64

import cv2


class FrameEncoder:
    """BGR frame → base64 JPEG text (wire format for the viewer server)."""

    @staticmethod
    def encode(frame):
        ok, buffer = cv2.imencode(".jpg", frame)
        if not ok:
            return None
        return base64.b64encode(buffer).decode("utf-8")
