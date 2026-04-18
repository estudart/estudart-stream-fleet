import base64

import cv2
import numpy as np


class FrameDecoder:
    @staticmethod
    def decode(frame):
        ok, buffer = cv2.imencode('.jpg', frame)
        if not ok:
            return None
        return base64.b64encode(buffer).decode('utf-8')

    @staticmethod
    def text_to_frame(data: str):
        img_bytes = base64.b64decode(data)
        np_arr = np.frombuffer(img_bytes, dtype=np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        return frame