import base64

import cv2


class FrameDecoder:
    @staticmethod
    def decode(frame):
        ok, buffer = cv2.imencode('.jpg', frame)
        if not ok:
            return None
        return base64.b64encode(buffer).decode('utf-8')