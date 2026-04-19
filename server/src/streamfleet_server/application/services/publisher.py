import asyncio

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from src.streamfleet_server.infrastructure.decoding.jpeg_bgr_decoder import decode_jpeg_base64_to_bgr
from src.streamfleet_server.infrastructure.redis.redis_adapter import RedisAdapter


class Publisher:
    """Application service: publish text payloads to Redis channels (e.g. base64 JPEG from clients)."""

    def __init__(self, redis_adapter: RedisAdapter):
        self._redis = redis_adapter

    def publish(self, channel: str, message: str) -> bool:
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
                frame = await decode_jpeg_base64_to_bgr(data)
                if frame is None:
                    continue
                await asyncio.sleep(0)
                # Redis pub/sub payloads must be strings; wire format is the same base64 text.
                self.publish(channel=str(client_id), message=data)
        except WebSocketDisconnect:
            pass
        except Exception as err:
            print(f"Publish connection closed: {err}")