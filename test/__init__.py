import glob
import os

import cv2

from src.hand_detector import detect_hand_in_image
from src.image_ops import read_img


def test_detection_on_image(img_path):
    detect_hand_in_image(read_img(img_path))


def test_detection_on_directory():
    dir_path = r'data\test'
    for f in os.listdir(dir_path):
        test_detection_on_image(os.path.join(dir_path, f))
