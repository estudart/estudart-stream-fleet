import asyncio

import cv2
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.infrastructure.decoding.jpeg_bgr_decoder import decode_jpeg_base64_to_bgr
from src.streamfleet_server.presentation.app import app
from src.streamfleet_server.presentation.dependencies import get_publisher
from src.streamfleet_server.presentation.helpers import (
    _DRONE_STREAM_WINDOW,
    close_preview_window_named,
)


@app.websocket("/v1/ws/publish")
async def publish(websocket: WebSocket):
    """
    Receive base64 JPEG frames over WebSocket, optional local preview, and publish the
    same payload string to Redis (subscribers must use the same ``channel`` query param).
    """
    await websocket.accept()

    client_id = id(websocket)
    print(client_id)

    publisher = get_publisher()

    try:
        while True:
            data = await websocket.receive_text()
            frame = decode_jpeg_base64_to_bgr(data)
            if frame is None:
                continue
            await asyncio.sleep(0)
            # Redis pub/sub payloads must be strings; wire format is the same base64 text.
            publisher.publish(channel=client_id, message=data)
    except WebSocketDisconnect:
        pass
    except Exception as err:
        print(f"Publish connection closed: {err}")
