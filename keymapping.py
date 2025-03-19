import pyautogui
import json
import time
from pynput import mouse

# Global variables to store clicks
clicks = []
key_order = ["A", "S", "D", "F", "J", "K", "L", ";"]
first_click_ignored = False


def on_click(x, y, button, pressed):
    """
    Callback function to capture mouse clicks.
    """
    global first_click_ignored

    if pressed:
        # Ignore the first click
        if not first_click_ignored:
            first_click_ignored = True
            print("First click ignored. Now recording actual key positions...")
            return True

        print(f"Captured click at: ({x}, {y}) for key: {key_order[len(clicks)]}")
        clicks.append((x, y))

        # Stop listener after capturing all keys
        if len(clicks) == len(key_order):
            return False


def capture_clicks():
    """
    Capture mouse clicks globally, ignoring the first click.
    """
    print("Please click anywhere once to start (this click will be ignored)")
    print(f"Then click on the keys in the following order: {', '.join(key_order)}")

    # Set up the mouse listener
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return clicks


def save_coordinates(coordinates, filename="key_mapping.json"):
    """
    Save the captured coordinates to a JSON file.

    :param coordinates: List of (x, y) coordinates
    :param filename: Name of the file to save the coordinates
    """
    key_mapping = {key: coord for key, coord in zip(key_order, coordinates)}

    with open(filename, 'w') as file:
        json.dump(key_mapping, file, indent=4)

    print(f"Coordinates saved to {filename}")


def main():
    # Capture clicks
    coordinates = capture_clicks()

    # Save the coordinates to a file
    save_coordinates(coordinates)


if __name__ == "__main__":
    main()