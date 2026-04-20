import asyncio

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.infrastructure.redis.redis_adapter import RedisAdapter


class Publisher:
    """Application service: publish text payloads to Redis channels (e.g. base64 JPEG from clients)."""

    def __init__(self, redis_adapter: RedisAdapter):
        self._redis = redis_adapter

    async def publish(self, channel: str, message: str) -> bool:
        try:
            self._redis.publish(channel=channel, message=message)
            return True
        except Exception as err:
            print(f"Redis publish failed: {err}")
            return False

    async def run(self, websocket: WebSocket):
        client_id = id(websocket)
        print(client_id)
        try:
            while True:
                data = await websocket.receive_text()
                if data is None:
                    continue

                await self.publish(channel=str(client_id), message=data)
        except WebSocketDisconnect:
            pass
        except Exception as err:
            print(f"Publish connection closed: {err}")