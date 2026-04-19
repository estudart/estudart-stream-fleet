from fastapi import WebSocket

from src.streamfleet_server.presentation.app import app
from src.streamfleet_server.presentation.dependencies import get_publisher


@app.websocket("/v1/ws/publish")
async def publish(websocket: WebSocket):
    """
    Receive base64 JPEG frames over WebSocket, optional local preview, and publish the
    same payload string to Redis (subscribers must use the same ``channel`` query param).
    """
    await websocket.accept()

    publisher = get_publisher()
    await publisher.run(websocket=websocket)
