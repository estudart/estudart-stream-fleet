from src.application.services.computer_streamer import ComputerStreamer
from src.application.services.drone_streamer import DroneStreamer
from src.application.services.frame_decoder import FrameDecoder
from src.infrastructure.tello.tello_adapter import TelloAdapter
from src.infrastructure.webcam_adapter import WebcamAdapter
from src.infrastructure.websocket_adapter import WebSocketAdapter

_tello_adapter: TelloAdapter = None
_webcam_adapter: WebcamAdapter = None
_drone_streamer: DroneStreamer = None
_computer_streamer: ComputerStreamer = None
_websocket_adapter: WebSocketAdapter = None
_frame_decoder: FrameDecoder = None

def get_frame_decoder():
    global _frame_decoder
    if _frame_decoder is None:
        _frame_decoder = FrameDecoder()
    return _frame_decoder

def get_websocket_adapter():
    global _websocket_adapter
    if _websocket_adapter is None:
        frame_decoder = get_frame_decoder()
        _websocket_adapter = WebSocketAdapter(
            uri="ws://localhost:8000/v1/ws/stream",
            frame_decoder=frame_decoder)
    return _websocket_adapter

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
        websocket_adapter = get_websocket_adapter()
        _drone_streamer = DroneStreamer(
            stream_adapter=stream_adapter,
            websocket_adapter=websocket_adapter)
    return _drone_streamer

def get_computer_streamer():
    global _computer_streamer
    if _computer_streamer is None:
        stream_adapter = get_webcam_adapter()
        websocket_adapter = get_websocket_adapter()
        _computer_streamer = ComputerStreamer(
            stream_adapter=stream_adapter,
            websocket_adapter=websocket_adapter)
    return _computer_streamer
