import pyautogui


class TypingController:
    def type_text(self, text):
        """
        Simulate typing the provided text.

        :param text: Text to type
        """
        pyautogui.write(text)