import asyncio

import websockets

from src.streamfleet_client.infrastructure.encoding.frame_encoder import FrameEncoder


class WebSocketSender:
    """Infrastructure: outbound WebSocket to the viewer server."""

    def __init__(self, uri: str, frame_encoder: FrameEncoder):
        self.uri = uri
        self.frame_encoder = frame_encoder
        self._running = None

    def stop(self):
        self._running = False

    async def stream(self, frame_read):
        self._running = True
        async with websockets.connect(self.uri) as ws:
            while self._running:
                frame = frame_read.frame
                if frame is None:
                    await asyncio.sleep(0.01)
                    continue

                jpg_as_text = self.frame_encoder.encode(frame)
                if jpg_as_text is None:
                    await asyncio.sleep(0.01)
                    continue
                await ws.send(jpg_as_text)

                await asyncio.sleep(0.03)
