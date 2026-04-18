import asyncio

import cv2
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.infrastructure.decoding.jpeg_bgr_decoder import decode_jpeg_base64_to_bgr
from src.streamfleet_server.presentation.app import app
from src.streamfleet_server.presentation.helpers import (
    _DRONE_STREAM_WINDOW,
    close_preview_window_named,
)


@app.websocket("/v1/ws/test")
async def terminal_test(websocket: WebSocket):
    await websocket.accept()

    client_id = id(websocket)
    window_name = f"{_DRONE_STREAM_WINDOW}_{client_id}"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            data = await websocket.receive_text()
            frame = decode_jpeg_base64_to_bgr(data)
            if frame is None:
                continue
            cv2.imshow(window_name, frame)
            await asyncio.sleep(0)
            cv2.waitKey(1)
    except WebSocketDisconnect:
        pass
    except Exception as err:
        print(f"Connection closed: {err}")
    finally:
        close_preview_window_named(window_name)