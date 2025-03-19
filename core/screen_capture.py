from PIL import ImageGrab


class ScreenCapture:
    def capture_screen(self, coords):
        """
        Capture a screenshot of the specified screen area.

        :param coords: List of coordinates [x1, y1, x2, y2]
        :return: PIL Image object
        """
        if not coords or len(coords) != 4:
            raise ValueError("Invalid coordinates provided.")

        x1, y1, x2, y2 = coords
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        return screenshot