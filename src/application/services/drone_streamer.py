import asyncio

import cv2

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
        try:
            self.stream_adapter.streamoff()
            cv2.destroyAllWindows()
        except Exception as err:
            print(f"Could not stop streaming, reason: {err}")

    async def start_streaming(self):
        try:
            self.stream_adapter.streamon()
            frame_read = self.stream_adapter.get_frame_read()

            await self.websocket_adapter.stream(frame_read)

        finally:
            self.stop_streaming()

        
