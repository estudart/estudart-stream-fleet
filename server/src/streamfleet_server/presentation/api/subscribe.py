import asyncio

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.presentation.app import app
from src.streamfleet_server.presentation.dependencies import get_redis_adapter


@app.websocket("/ws/subscribe")
async def subscribe(websocket: WebSocket):
    """
    Stream Redis pub/sub messages to the WebSocket client.
    Required query param: ``channel`` — must match the publisher channel (see ``/v1/ws/publish``).
    """
    await websocket.accept()

    channel = websocket.query_params.get("channel")
    if not channel:
        await websocket.close(code=1008)
        return

    redis = get_redis_adapter()
    pubsub = redis.create_pubsub(channel)

    try:
        while True:
            msg = await asyncio.to_thread(
                lambda: pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0),
            )
            if not msg or msg.get("type") != "message":
                continue
            payload = msg.get("data")
            if payload is None:
                continue
            await websocket.send_text(payload)
    except WebSocketDisconnect:  # client disconnect
        pass
    except Exception as err:
        print(f"Subscribe connection closed: {err}")
    finally:
        try:
            pubsub.close()
        except Exception:
            pass
