import asyncio

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.infrastructure.redis.redis_adapter import RedisAdapter


class Consumer:
    """Application service: publish text payloads to Redis channels (e.g. base64 JPEG from clients)."""

    def __init__(self, redis_adapter: RedisAdapter):
        self._redis = redis_adapter


    async def consume(self, channel: str, websocket: WebSocket):
        pubsub = self._redis.create_pubsub(channel)

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