import asyncio
import websockets
import base64
import cv2

from src.application.services.frame_decoder import FrameDecoder

class WebSocketAdapter:
    def __init__(self, uri: str, frame_decoder: FrameDecoder):
        self.uri = uri
        self.frame_decoder = frame_decoder
        self._running = None

    def stop(self):
        self._running = False

    async def stream(self, frame_read):
        self._running = True
        async with websockets.connect(self.uri) as ws:
            while self._running == True:
                frame = frame_read.frame
                if frame is None:
                    await asyncio.sleep(0.01)
                    continue

                jpg_as_text = self.frame_decoder.decode(frame=frame)
                await ws.send(jpg_as_text)

                await asyncio.sleep(0.03)
