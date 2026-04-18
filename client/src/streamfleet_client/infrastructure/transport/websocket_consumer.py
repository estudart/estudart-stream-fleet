from collections.abc import AsyncIterator
from urllib.parse import urlencode

import websockets


class WebSocketConsumer:
    """
    Subscribe-side WebSocket client: connects to the server's Redis fan-out endpoint
    ``/v1/ws/subscribe?channel=...`` and yields incoming text frames (e.g. base64 JPEG).
    """

    def __init__(
        self,
        channel_id: str,
        *,
        base_url: str = "ws://localhost:8000",
    ):
        self._channel_id = channel_id
        self._base_url = base_url.rstrip("/")

    @property
    def channel_id(self) -> str:
        return self._channel_id

    @property
    def uri(self) -> str:
        query = urlencode({"channel": self._channel_id})
        return f"{self._base_url}/v1/ws/subscribe?{query}"

    async def get_messages(self) -> AsyncIterator[str]:
        """
        Async generator of text frames from the server — use ``async for``, not ``await``::

            async for payload in consumer.get_messages():
                ...
        """
        async with websockets.connect(self.uri) as ws:
            async for raw in ws:
                if isinstance(raw, bytes):
                    yield raw.decode("utf-8", errors="replace")
                else:
                    yield raw
