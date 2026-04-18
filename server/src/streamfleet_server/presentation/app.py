from fastapi import FastAPI
import cv2

_DRONE_STREAM_WINDOW = "Drone Stream"

app = FastAPI()

def _close_drone_stream_window() -> None:
    """
    destroyWindow/destroyAllWindows only schedule closing; HighGUI must still process
    events or the window stays frozen on the last frame (common on macOS).
    """
    try:
        cv2.destroyWindow(_DRONE_STREAM_WINDOW)
    except cv2.error:
        pass
    for _ in range(128):
        cv2.waitKey(1)
    try:
        cv2.destroyAllWindows()
    except cv2.error:
        pass
    cv2.waitKey(1)
