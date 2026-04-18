import asyncio

import cv2
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.infrastructure.decoding.jpeg_bgr_decoder import decode_jpeg_base64_to_bgr
from src.streamfleet_server.application.services.preview_window_service import (
    app,
    _DRONE_STREAM_WINDOW,
    _close_drone_stream_window,
)


@app.websocket("/v1/ws/stream")
async def websocket_stream(websocket: WebSocket):
    await websocket.accept()

    cv2.namedWindow(_DRONE_STREAM_WINDOW, cv2.WINDOW_NORMAL)

    try:
        while True:
            data = await websocket.receive_text()
            frame = decode_jpeg_base64_to_bgr(data)
            if frame is None:
                continue
            cv2.imshow(_DRONE_STREAM_WINDOW, frame)
            await asyncio.sleep(0)
            cv2.waitKey(1)
    except WebSocketDisconnect:
        pass
    except Exception as err:
        print(f"Connection closed: {err}")
    finally:
        _close_drone_stream_window()
