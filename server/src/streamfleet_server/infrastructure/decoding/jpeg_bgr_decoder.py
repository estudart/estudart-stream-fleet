import base64

import cv2
import numpy as np


def decode_jpeg_base64_to_bgr(data: str):
    """Decode raw base64 JPEG text to a BGR ndarray (OpenCV)."""
    img_bytes = base64.b64decode(data)
    np_arr = np.frombuffer(img_bytes, dtype=np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
