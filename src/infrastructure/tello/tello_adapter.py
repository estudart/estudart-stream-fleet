from djitellopy import Tello, BackgroundFrameRead

class TelloAdapter:
    def __init__(self):
        self.tello = Tello()
        self._connect()

    def _connect(self) -> bool:
        try:
            self.tello.connect()
            return True
        except Exception as err:
            print(err)
            return False

    def get_battery(self):
        return self.tello.get_battery()

    def streamon(self) -> bool:
        try:
            self.tello.streamon()
            return True
        except Exception as err:
            print(err)
            return False

    def streamoff(self) -> bool:
        try:
            self.tello.streamoff()
            return True
        except Exception as err:
            print(err)
            return False

    def get_frame_read(self) -> BackgroundFrameRead:
        try:
            frame = self.tello.get_frame_read()
            return frame
        except Exception as err:
            print(err)

    def takeoff(self) -> bool:
        try:
            self.tello.takeoff()
            return True
        except Exception as err:
            print(err)
            return False

    def land(self) -> bool:
        try:
            self.tello.land()
            return True
        except Exception as err:
            print(err)
            return False

    def moveup(self, distance: int) -> bool:
        try:
            self.tello.move_up(distance)
            return True
        except Exception as err:
            print(err)
            return False
