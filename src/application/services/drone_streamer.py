import asyncio

from src.infrastructure.stream_adapter import StreamAdapter
from src.infrastructure.websocket_adapter import WebSocketAdapter

class DroneStreamer:
    def __init__(
        self, 
        stream_adapter: StreamAdapter, 
        websocket_adapter: WebSocketAdapter
    ):
        self.stream_adapter = stream_adapter
        self.websocket_adapter = websocket_adapter

    def stop_streaming(self):
        pass

    async def start_streaming(self):
        try:
            if not self.stream_adapter.streamon():
                return
            frame_read = self.stream_adapter.get_frame_read()
            if frame_read is None:
                return

            await self.websocket_adapter.stream(frame_read)

        finally:
            self.stop_streaming()
