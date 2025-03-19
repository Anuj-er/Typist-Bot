import pyautogui
import json
from PIL import ImageGrab
import time

# Define color thresholds
BLUE_THRESHOLD = (50, 50, 200)  # RGB values for blue
COLOR_THRESHOLD = 30  # Allow some variation in color detection
SEARCH_RADIUS = 10  # Increased radius to detect circles better


def load_key_mapping(filename="key_mapping.json"):
    """Load the key coordinates from the JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)


def is_blue(pixel):
    """Check if a pixel is close to blue."""
    r, g, b = pixel[:3]  # Only use the first three values (R, G, B)
    # Check if the pixel is close to blue (low R, low G, high B)
    return (r < BLUE_THRESHOLD[0] + COLOR_THRESHOLD and
            g < BLUE_THRESHOLD[1] + COLOR_THRESHOLD and
            b > BLUE_THRESHOLD[2] - COLOR_THRESHOLD)


def detect_blue_circle(x, y, radius=SEARCH_RADIUS):
    """
    Detect if there's a blue circle around the given coordinate.
    Returns True if a significant number of blue pixels are found.
    """
    # Convert coordinates to integers
    x, y = int(x), int(y)

    # Define the region to check
    left = x - radius
    top = y - radius
    right = x + radius
    bottom = y + radius

    # Capture the region
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    pixels = list(screenshot.getdata())

    # Count blue pixels
    blue_pixel_count = sum(1 for p in pixels if is_blue(p))
    total_pixels = len(pixels)

    # If more than 25% of pixels are blue, consider it a blue circle
    return blue_pixel_count / total_pixels > 0.25


def main():
    key_mapping = load_key_mapping()

    try:
        print("Monitoring for blue circles. Press Ctrl+C to exit.")
        while True:
            # Get current mouse position
            mouse_x, mouse_y = pyautogui.position()

            for key, coord in key_mapping.items():
                x, y = coord
                if detect_blue_circle(x, y):
                    print(f"Blue circle detected at key: {key}. Pressing key: {key}")
                    pyautogui.press(key)
                    # Short pause to avoid multiple detections
                    time.sleep(0.1)

            # Check every 0.05 seconds
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("Monitoring stopped.")


if __name__ == "__main__":
    main()