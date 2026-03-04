import pyautogui
import random
import time

pyautogui.FAILSAFE = False

# Get screen dimensions
width, height = pyautogui.size()

print("Press Ctrl-C to quit.")

try:
    while True:
        # Get current mouse position
        current_x, current_y = pyautogui.position()

        # Define the maximum offset for the mouse movement
        max_offset = 50

        # Generate random offsets
        offset_x = random.randint(-max_offset, max_offset)
        offset_y = random.randint(-max_offset, max_offset)

        # Calculate new coordinates, making sure they are within screen bounds
        x = max(0, min(width - 1, current_x + offset_x))
        y = max(0, min(height - 1, current_y + offset_y))

        # Move the mouse to the new coordinates
        pyautogui.moveTo(x, y, duration=0.5)

        # Wait for a random time before moving again (e.g., between 1 and 3 seconds)
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
except KeyboardInterrupt:
    print("\nScript terminated.") 