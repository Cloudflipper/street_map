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
from tqdm import tqdm

def map_name(index):
    return chr(index + 65) if index < 26 else 'Z' + chr(index + 65 - 26) + chr(index + 65 - 26)

def get_original_pic(index_x, index_y):
    driver = webdriver.Chrome()
    driver.maximize_window()  # Maximize browser window for better screenshot area
    base_x, base_y = 13386335, 3583355  # Base coordinates (Suzhou)
    web_name = f"http://map.baidu.com/@{base_x + 7000 * index_x},{base_y + 4000 * index_y},15.5z"
    driver.get(web_name)
    time.sleep(random.randrange(15, 18, 1))
    filename = f"pics3/{map_name(index_x)}_{map_name(index_y)}.png"
    driver.save_screenshot(filename)
    file_chop(filename)

def file_chop(file):
    img = cv2.imread(file)
    cropped = img[90:796, 65:1301]  # Crop to remove browser frame
    cv2.imwrite(file, cropped)

def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_WIDTH, IMAGE_ROW * IMAGE_HEIGHT))
    for y in tqdm(range(1, IMAGE_ROW + 1)):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[(y - 1) + IMAGE_ROW * (x - 1)]).resize(
                (IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_WIDTH, (IMAGE_ROW - y) * IMAGE_HEIGHT))
    to_image.save(IMAGE_SAVE_PATH)

for index_x in range(19):
    for index_y in range(41):
        if index_x <= 1 or (index_x == 2 and index_y <= 12):
            continue
        get_original_pic(index_x, index_y)

IMAGES_PATH = 'pics3/'
IMAGE_WIDTH = 1236
IMAGE_HEIGHT = 706
IMAGE_ROW = 41
IMAGE_COLUMN = 19
IMAGE_SAVE_PATH = IMAGES_PATH + 'Suzhou.png'

picName_list = os.listdir(IMAGES_PATH)
image_list = [fn for fn in picName_list if fn.endswith('.png')]
image_names = sorted(image_list)

if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("Mismatch between expected and actual number of images!")

image_compose()



