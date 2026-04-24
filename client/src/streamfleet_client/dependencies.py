from typing import Optional

from streamfleet_client.adapters.tello.tello_adapter import TelloAdapter
from streamfleet_client.adapters.webcam_adapter import WebcamAdapter
from streamfleet_client.encoding.frame_encoder import FrameEncoder
from streamfleet_client.streamers.computer_streamer import ComputerStreamer
from streamfleet_client.streamers.drone_streamer import DroneStreamer
from streamfleet_client.transport.websocket_sender import WebSocketSender

_tello_adapter: Optional[TelloAdapter] = None
_webcam_adapter: Optional[WebcamAdapter] = None
_drone_streamer: Optional[DroneStreamer] = None
_computer_streamer: Optional[ComputerStreamer] = None
_websocket_sender: Optional[WebSocketSender] = None
_frame_encoder: Optional[FrameEncoder] = None


def get_frame_encoder():
    global _frame_encoder
    if _frame_encoder is None:
        _frame_encoder = FrameEncoder()
    return _frame_encoder


def get_websocket_sender():
    global _websocket_sender
    if _websocket_sender is None:
        frame_encoder = get_frame_encoder()
        _websocket_sender = WebSocketSender(
            uri="ws://localhost:8000/v1/ws/stream",
            frame_encoder=frame_encoder,
        )
    return _websocket_sender


def get_tello_adapter():
    global _tello_adapter
    if _tello_adapter is None:
        _tello_adapter = TelloAdapter()
    return _tello_adapter


def get_webcam_adapter():
    global _webcam_adapter
    if _webcam_adapter is None:
        _webcam_adapter = WebcamAdapter(device_index=0)
    return _webcam_adapter


def get_drone_streamer():
    global _drone_streamer
    if _drone_streamer is None:
        stream_adapter = get_tello_adapter()
        websocket_sender = get_websocket_sender()
        _drone_streamer = DroneStreamer(
            stream_adapter=stream_adapter,
            websocket_sender=websocket_sender,
        )
    return _drone_streamer


def get_computer_streamer():
    global _computer_streamer
    if _computer_streamer is None:
        stream_adapter = get_webcam_adapter()
        websocket_sender = get_websocket_sender()
        _computer_streamer = ComputerStreamer(
            stream_adapter=stream_adapter,
            websocket_sender=websocket_sender,
        )
    return _computer_streamer
