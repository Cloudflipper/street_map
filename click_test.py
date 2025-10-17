# click_test.py
from ctypes import windll
import win32api
import win32con
import time
import pyautogui as pag

try:
    while True:
        print("Press Ctrl-C to stop.")
        screenWidth, screenHeight = pag.size()  # Get screen resolution
        x, y = pag.position()  # Get current mouse position
        print(f"Screen size: ({screenWidth}, {screenHeight}), Position: ({x}, {y})\n")
        time.sleep(1)
except KeyboardInterrupt:
    print('Program ended.')
