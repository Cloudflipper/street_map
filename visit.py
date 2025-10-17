from selenium import webdriver
import time
import win32api
import win32con
import random
from ctypes import windll
import cv2
import numpy as np
from PIL import Image
import PIL.Image as Image
import os

def get_original_pic(index_x, index_y):
    driver = webdriver.Chrome()
    driver.maximize_window()
    base_x, base_y = 13517926, 3614804  # Base coordinates (Shanghai)
    web_name = f"http://map.baidu.com/@{base_x + 7000 * index_x},{base_y + 4000 * index_y},15.5z"
    driver.get(web_name)
    time.sleep(random.randrange(300, 500, 5) / 100)
    windll.user32.SetCursorPos(1891, 880)
    time.sleep(random.randrange(70, 120, 1) / 100)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 900, 300)
    time.sleep(random.randrange(40, 60, 1) / 1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 900, 300)
    time.sleep(random.randrange(70, 120, 1) / 100)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 900, 300)
    time.sleep(random.randrange(40, 60, 1) / 1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 900, 300)
    time.sleep(random.randrange(8, 12, 1))

for index_x in range(-7, 11):
    for index_y in range(15, 17):
        get_original_pic(index_x, index_y)
