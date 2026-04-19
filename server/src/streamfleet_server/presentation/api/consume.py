from fastapi import WebSocket

from src.streamfleet_server.presentation.app import app
from src.streamfleet_server.presentation.dependencies import get_consumer


@app.websocket("/v1/ws/consume")
async def consume(websocket: WebSocket):
    """
    Stream Redis pub/sub messages to the WebSocket client.
    Required query param: ``channel`` — must match the publisher channel (see ``/v1/ws/publish``).
    """
    await websocket.accept()

    channel = websocket.query_params.get("channel")
    if not channel:
        await websocket.close(code=1008)
        return

    consumer = get_consumer()
    await consumer.consume(
        channel=channel,
        websocket=websocket,
    )
