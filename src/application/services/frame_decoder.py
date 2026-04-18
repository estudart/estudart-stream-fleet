

class FrameDecoder:
    @staticmethod
    def decode(frame):
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        return jpg_as_text