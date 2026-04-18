from src.streamfleet_client.domain.ports.stream_adapter import StreamAdapter
from src.streamfleet_client.infrastructure.transport.websocket_sender import WebSocketSender


class DroneStreamer:
    def __init__(
        self,
        stream_adapter: StreamAdapter,
        websocket_sender: WebSocketSender,
    ):
        self.stream_adapter = stream_adapter
        self.websocket_sender = websocket_sender

    def stop_streaming(self):
        pass

    async def start_streaming(self):
        try:
            if not self.stream_adapter.streamon():
                return
            frame_read = self.stream_adapter.get_frame_read()
            if frame_read is None:
                return

            await self.websocket_sender.stream(frame_read)

        finally:
            self.stop_streaming()
