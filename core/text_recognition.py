import pytesseract
from PIL import Image


class TextRecognition:
    def recognize_text(self, image):
        """
        Recognize text from an image using OCR.

        :param image: PIL Image object
        :return: Recognized text as a string
        """
        text = pytesseract.image_to_string(image)
        return text.strip()