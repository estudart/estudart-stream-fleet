import cv2
from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

from src.presentation.dependencies import get_frame_decoder

app = FastAPI()


@app.websocket("/v1/ws/stream")
async def websocket_stream(websocket: WebSocket):
    frame_decoder = get_frame_decoder()
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            frame = frame_decoder.text_to_frame(data=data)
            if frame is None:
                continue
            cv2.imshow("Drone Stream", frame)
            cv2.waitKey(1)
    except WebSocketDisconnect:
        pass
    except Exception as err:
        print(f"Connection closed: {err}")
    finally:
        cv2.destroyAllWindows()
