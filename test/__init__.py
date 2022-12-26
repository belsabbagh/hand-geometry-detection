import glob
import os

import cv2

from src.hand_detector import detect_hand_in_image
from src.image_ops import read_img
from src.image_ops.scale_img import scale_img



def test_detection_on_image(img_path):
    img = scale_img(read_img(img_path), 0.4)
    detect_hand_in_image(img)


def test_detection_on_directory():
    dir_path = r'data\dorsal left\p'
    for f in os.listdir(dir_path):
        test_detection_on_image(os.path.join(dir_path, f))
